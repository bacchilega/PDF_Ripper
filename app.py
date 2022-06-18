import csv
import pdfplumber
import os

#setting directory
directory = r'C:\Users\Pterodattilo\Desktop\pdf_ripper'

#list all .PDF in the directory
for filename in os.listdir(directory):
    if filename.endswith('.pdf'):

        fullpath = os.path.join(directory, filename)
    
        with pdfplumber.open(fullpath) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                print(text)
       
        with open('csvfile.csv','wb') as file:
            b = bytes(text, 'utf-8')
            file.write(b)
            file.close()



       # with open('csvfile.csv','wb') as file:
       #     for line in text2:
       #         file.write(text2.encode())
       #         file.write('\n')

       
#file.write(text2.encode())

#        with open('csvfile.csv','rb') as f:
#            lines = [x.decode('utf8').strip() for x in f.readlines()]
#            for lines in text:
#                f.write(lines)
#                f.write('\n')

#    lines = [x.decode('utf8').strip() for x in f.readlines()]
