import os
import docx
import PyPDF2
import pandas as pd

def process(directory):
    documents = []
    for root, dirs, files in os.walk(directory):  # 使用os.walk来递归地处理文件夹和子文件夹
        for filename in files:
            file_path = os.path.join(root, filename)  # os.walk提供了文件的root路径，可以用它来生成完整的文件路径
            print("Processing file: ", file_path)  # 打印正在处理的文件名
            if filename.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    print("Content: ", content)  # 打印文件内容
                    documents.append({'title': filename, 'content': content})
            elif filename.endswith('.docx'):
                doc = docx.Document(file_path)
                content = ' '.join([p.text for p in doc.paragraphs])
                print("Content: ", content)  # 打印文件内容
                documents.append({'title': filename, 'content': content})
            elif filename.endswith('.pdf'):
                pdf_file_obj = open(file_path, 'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
                content = ' '.join([pdf_reader.getPage(i).extractText() for i in range(pdf_reader.numPages)])
                print("Content: ", content)  # 打印文件内容
                documents.append({'title': filename, 'content': content})
            elif filename.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(file_path)
                content = ' '.join(df.to_string(index=False).split('\n'))
                print("Content: ", content)  # 打印文件内容
                documents.append({'title': filename, 'content': content})
    return documents
