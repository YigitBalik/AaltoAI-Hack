# AaltoAI-Hack
AaltoAI Hackathon, Microsoft GenAI Challenge


# AI-Assisted RFP Processing Pipeline
<img src="./templates/logo.png" alt="drawing" style="width:200px;"/>

## Overview
In the competitive B2B sector, responding efficiently and accurately to Requests for Proposals (RFPs) is crucial for securing new contracts and investments. Our global company, which manufactures and sells a diverse range of products, is embracing Generative AI to enhance our response process to RFPs. This project aims to reduce manual labor, accelerate response times, and improve the accuracy of our proposals.

## Challenge
We are tasked with developing a Generative AI system that can:
- *Extract RFP Details*: Process RFP documents in various formats PDF and extract critical information such as sender's details, RFP issue and due dates, and specific requirements (product specs, technical drawings).
- *Determine Suitable Products*: Identify the most appropriate products from our catalog that match the RFP details, considering size, dimensions, type, weight, and power requirements.
- *Craft Proposals*: Auto-populate our proposal template with the selected products, pricing, and terms of delivery.
- *Obtain Approval*: Ensure the proposal's economic feasibility based on defined metrics.
- *Return Proposal PDF*: Generate and deliver a finalized proposal in PDF format.

## Solution
To address this challenge, we have implemented an AI-powered pipeline that integrates various AI models and techniques to automate the RFP response process. The diagram below illustrates the proposed solution:

![AI Pipeline Diagram](./templates/system1.jpg)

## Pipeline Stages
1. *Upload RFP*: Users can upload RFP documents directly to the system.
2. *Parse Text*: The system extracts text from the uploaded documents.
3. *Generate JSON*: Extracted text is converted into a structured JSON format.
4. *Vectorize Query*: JSON data is used to create a vectorized representation for similarity searching.
5. *Upstash*: Utilize Upstash's vector database to find similar past RFP responses.
6. *Hugging Face*: Leverage Hugging Face models for additional AI processing.
7. *Proposal Content*: Compile the content for the proposal based on the best matches.
8. *Best Match*: Determine the top 3 most suitable responses.
9. *Generate Proposal*: Populate the proposal template and create a draft.
10. *Finalize PDF*: Convert the approved proposal into a PDF document.

## Real-World Impact


1. Increased Efficiency: By automating the process of extracting RFP details, identifying suitable products, and crafting proposals, the system significantly reduces manual labor and accelerates response times. This efficiency gain allows the company to handle a higher volume of RFPs and respond more promptly to customer inquiries, potentially leading to increased business opportunities.
2. Improved Accuracy: With AI assistance, the system can analyze RFPs more comprehensively and accurately identify the most suitable products from the company's catalog. This accuracy reduces the risk of errors in proposals, ensuring that they align closely with the customer's requirements and preferences. As a result, the company can enhance its reputation for delivering tailored and precise solutions to clients.
3. Enhanced Customer Satisfaction: Faster response times and more accurate proposals contribute to improved customer satisfaction. Clients receive timely and relevant proposals that demonstrate a deep understanding of their needs, increasing the likelihood of securing contracts and fostering long-term relationships. Satisfied customers are more likely to repeat business and recommend the company to others, leading to sustainable growth and success.
4. Resource Optimization: By streamlining the RFP response process, the company can allocate human resources more effectively. Employees can focus on higher-value tasks such as refining proposal strategies, negotiating terms, and cultivating client relationships, rather than spending time on repetitive administrative tasks. This optimization of resources enhances overall productivity and allows employees to contribute more strategically to the company's objectives.
5. Competitive Advantage: Embracing AI technology for RFP processing gives the company a competitive edge in the B2B sector. The ability to respond quickly and accurately to RFPs demonstrates agility and innovation, distinguishing the company from competitors and positioning it as a preferred partner for potential clients. This competitive advantage can lead to increased market share, revenue growth, and sustained business success.

Overall, the AI-Assisted RFP Processing Pipeline has the potential to revolutionize the company's approach to handling RFPs, driving efficiency, accuracy, and customer satisfaction while positioning the company for long-term success in a competitive market landscape.

## Future Plans
1. Extend input types: Accept DOCx, JPG documents in addition to PDF.
2. Improve pipeline for considering profit maximization.
