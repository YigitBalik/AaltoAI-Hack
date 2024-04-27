from flask import render_template, request, redirect, send_file, flash, send_from_directory
from forms import RFP
from pyhtml2pdf import converter
import os
from __main__ import app
from werkzeug.utils import secure_filename
from time import time
import PyPDF2
from prompter import Prompter

class Controller(object):
    def __init__(self):
        self.ALLOWED_EXTENSIONS = {'pdf'}
        self.prompter = Prompter()

    def main(self):
        form = RFP()
        return render_template("main.html", form=form)
    
    def __allowed_file(self, filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS
    
    def __delete_uploads(self, filename):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    def pdf(self):
        return send_from_directory(app.config['UPLOAD_FOLDER'], 'sample.pdf')
        
    def execute(self):
        form = RFP()
        print(form.validate_on_submit())
        if form.validate_on_submit():
            file = request.files['file']
            if file.name == '':
                flash('No selected file')
                return redirect(request.url)
            if file and self.__allowed_file(file.filename):
                start_time = time()
                filename = secure_filename(form.file.data.filename)
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(path)

                
                with open(path, 'rb') as f:
                    # Create a PDF reader object
                    reader = PyPDF2.PdfReader(f)

                    # Get the number of pages in the PDF
                    num_pages = len(reader.pages)

                    # Extract the content from each page
                    content = ''
                    for page_num in range(num_pages):
                        page = reader.pages[page_num]
                        content += page.extract_text()

                customer_keywords = self.prompter.keywords(content)
                keywords = customer_keywords["keywords"]
                print(keywords)
                print("*******************")
                best_match = self.prompter.query_vectorDB(keywords)
                print(best_match)
                print("*******************")
                del customer_keywords["keywords"]
                proposal = self.prompter.generate_proposal(customer_keywords, best_match)
                
                if "`" == proposal[0]:
                    proposal = proposal[8:-3]

                print(proposal)
                f = open('./templates/results.html', "w")
                f.write(proposal)
                f.close()
                path = os.path.abspath('./templates/results.html')
                converter.convert(f'file:///{path}', os.path.join(app.config['UPLOAD_FOLDER'], 'sample.pdf'))

                duration = time() - start_time
                self.__delete_uploads(filename)
                return send_from_directory(app.config['UPLOAD_FOLDER'], 'sample.pdf')
            
        return render_template("main.html", form=form)