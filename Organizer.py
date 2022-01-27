import os
import shutil
doc_path = input('Enter the Address of folder you want to organise : ')
folder_name = input('Input folder name : ')
extensions = ('.docx','.pdf')

l = []
for  x in extensions:
    for item in os.listdir(doc_path): #listder takes the address of folder and gives tha name of the files
        if item.endswith(x):#it will check whether the file is ending with similar doc extensions or not
            l.append(item)
folder_path = ''
if len(l)!=0:
    folder_path = os.path.join(doc_path,folder_name) #combines the path of folder which we are organising and the name of the folder so that we can make folder to collect all documents or if it is pre existing then we will simply transfer the files in it
    if not(os.path.exists(folder_path)): #checking whether the path exists or not
        os.mkdir(folder_path)#to make folder
    for name  in l:
        file_path = os.path.join(doc_path,name)#geting paths of files
        shutil.move(file_path,folder_path)#moving files to folder with name folder_name
else :
    print('No Document file found')

''' what I learnt is
i forgot that mkdir gives error if folder alredy exist and
I could have cheked folder exists or not by using os.path.exists(folder address)->true or false
forgot to use list comprihenshions'''


