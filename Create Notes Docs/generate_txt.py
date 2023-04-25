import os
from functions.cut_file_paths import cut_path
from functions.extract_text import pdf_to_txt

directory = cut_path("Papers")
os.chdir(directory)

# Sweeps across the directory and checks the folders for pdf files to convert. Will not overwrite existing files.

for i in os.listdir():
    if not os.path.isdir(i):
        continue
    print(i)
    for f in os.listdir(i):
        if not f.endswith(".pdf"):
            continue
        pdf_to_txt(i,f, output_dir = i) 
        print(f)


