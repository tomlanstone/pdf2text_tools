import PyPDF2
import os

def read_page(reader, p):
    page = reader.pages[p]

    # extract text from page
    text = page.extract_text()
    raw_text = text.encode('unicode-escape').decode()
    raw_text = raw_text.replace(r"-\n","").replace(r"\n"," ")
    return raw_text

def pdf_to_txt(i,f, output_dir):
    ## Set up pdf reader
    file_name = f.replace(".pdf","")
    pdfFileObj = open(f'{i}/{f}', 'rb')
    reader = PyPDF2.PdfReader(pdfFileObj)
    
    ## Set up output file
    out_name = f"{output_dir}/{file_name}_notes.txt"
    if os.path.exists(out_name):
        print(f"exists")
        return
    else:
        out = open(out_name,"w")

    ## Extract text title page as first line of txt
      
    page = read_page(reader, 0)
    out.writelines(f"{page}\n\n")

    # close the open file objects
    pdfFileObj.close()
    out.close()