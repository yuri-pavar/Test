import os
from test import CreateField

def FileContent(root_path):
    set_of_file = set()
    list_of_text = []

    for path, dirs, files in os.walk(root_path): #get paths, directories and files in our root directory
       for fname in files:
           set_of_file.add(os.path.join(path, fname)) #inizializing our set_of_files with full path of files

    for file in set_of_file:
        with open(file) as data:
           list_of_text.append(data.readline()) #read the content of each file in list_of_text

    return list_of_text

def ContentOutput(list_of_text): #output
   for i in sorted(list_of_text):
        print(i)

root_path = r'C:\проекты\zry'
if CreateField(root_path):
    ContentOutput(FileContent(root_path))
