import sys

def cut_path(phrase):
    string = sys.argv[0].replace("\\","/")
    index = string.rfind(phrase)
    if index != -1:
        return f"{string[:index]}{phrase}" 
    else:
        return string