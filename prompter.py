import openai
from utils import template, customers
import json
from upstash_vector import Index
import csv
import requests
from tqdm import tqdm

import sys
sys.path.append('./..')
from ..secret import secret

class Prompter:

    def __init__(self):
        self.client = openai.OpenAI(api_key=secret.openai_api_key)
        self.model = "gpt-3.5-turbo"
        self.topk = 3
    
    def query_vectorDB(self, keywords):
        index = Index(url=secret.index_url, token=secret.index_token)
        API_URL = "https://api-inference.huggingface.co/models/mixedbread-ai/mxbai-embed-large-v1"
        headers = {"Authorization": secret.auth}

        payload = { "inputs": keywords }
        embedding = requests.post(API_URL, headers=headers, json=payload, timeout=None).json()
        print("---------EMBEDDING:", embedding)
        result=index.query(vector=embedding, top_k=self.topk,include_metadata=True,include_vectors=False)
        metas = [result[i].metadata for i in range(self.topk)]

        return str(metas)

    def keywords(self, content):
        print("KEYWORDS", content)
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a Request for Proposal (RFP) document analyzer.",
                },
                {
                    "role": "user",
                    "content": """
                        Objective: Generate a structured JSON representation of key information from an RFP document.

                        Fields to Extract:

                        Customer Name - Extract the name of the customer or company issuing the RFP.
                        Contact Details - Identify and extract any contact information such as phone numbers or physical addresses.
                        Email - Locate and extract the email address provided for correspondence.
                        Customer Requirements - List approximately 10 key terms that summarize the customer's requirements, separated by commas.
                        Expected JSON should look like:

                        {
                        "name": "customer name",
                        "email": "customer email",
                        "phone": "customer phone number",
                        "keywords": "keywords of customer requirements."
                        }

                        Only return JSON.
                    """,
                },
                {
                    "role": "user",
                    "content": content,
                }
            ],
            model=self.model,
        )

        
        if chat_completion.choices[0].message.content[0] == "`":
            print(chat_completion.choices[0].message.content[8:-3])
            return json.loads(chat_completion.choices[0].message.content[8:-3])
        print(chat_completion.choices[0].message.content)
        return json.loads(chat_completion.choices[0].message.content)

    def generate_proposal(self, content, best_matches):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "By using our content-based matching system we found best 3 product matches of customer's RFP in our catalog. Now you will act as a Proposal Creator. Here are the details of best 3 product matches."+ best_matches,
                },
                {
                    "role": "user",
                    "content": '''
                        You will create a proposal document based on the information extracted from the customer's Request for Proposal (RFP). Follow these guidelines to construct the offers:

                        - Calculate the original pricing and a discounted pricing offer considering the following:
                            * Early Payment Discount: Offer a discount for payments made within 3 months instead of the standard 1-year term.
                            * Bulk Purchase Discount: Determine a threshold number of products for a bulk purchase. Apply a discount once purchases exceed this threshold.
                            * Check customer database to update price to best matches. For example you can check if the customer is current or not, how much we sold them before, what is our proposal success 
                            ratio. If the customer is not current one, according to the similar companies in database please adjust discount ratio and price. The aim is increasing the profit by giving high prices to the possible customer. You can see customer database below.

                        - Document Preparation:
                            * The proposal should be formatted in HTML and designed to be visually appealing. Include our company logo ('logo.png') and use sophisticated color schemes with LaTeX-style fonts.
                            * Present both pricing options: the original and the discounted. Clearly layout the total proposal price which includes the number of products multiplied by the unit price. Show both the original and discounted totals.
                            * Ensure the proposal looks professional and does not disclose any profit-related information from our company.
                        
                        Your task is to craft a comprehensive and attractive proposal using the details from our product catalog and the customer's RFB, ensuring all information is presented clearly and attractively. Don't forget to include details of decided discounts.
                        Please include an appealing text in the proposal that can impress the potential customer to buy our product. Use a professional language to advertise our products.
                        
                            Return ONLY HTML code.

                            You can see our best 3 matches. Please do not offer anything outside of the matches.

                            IMPORTANT: PLEASE convert prices to be in range 800-1200.

                            FILL the following template. Do not create any additional HTML element. Just fill the required areas. If there is any missing information in the template such as due date and delivery date, generate them logically by yourself and fill the areas in the template.
            ''' + template + "\n our customer database:" + customers,
                },
                {
                    "role": "user",
                    "content": str(content),
                }
            ],
            model=self.model,
        )
        return chat_completion.choices[0].message.content

