import PyPDF2
import os

def read_page(reader, p):
    page = reader.pages[p]

    # extract text from page
    text = page.extract_text()
    raw_text = text.encode('unicode-escape').decode()
    raw_text = raw_text.replace(r"-\n","").replace(r"\n"," ")
    return raw_text

def pdf_to_txt(i,f, output_dir, rewrite = False):
    ## Set up pdf reader
    file_name = f.replace(".pdf","")
    pdfFileObj = open(f'{i}/{f}', 'rb')
    reader = PyPDF2.PdfReader(pdfFileObj)
    
    ## Set up output file
    out_name = f"{output_dir}/{file_name}.txt"
    # Insert code that will extract title
    # Change name of output to title
    # Change if statement to check for {title}.txt
    if os.path.exists(out_name):
        if not rewrite:
            print(f"exists")
            return
    else:
        out = open(out_name,"w")

    ## Extract text from pages and write to output
    for p in range(0,len(reader.pages)):
        
        page = read_page(reader, p)
        
        out.writelines(f"Page {p}\n")
        out.writelines(f"{page}\n")

    # close the open file objects
    pdfFileObj.close()
    out.close()