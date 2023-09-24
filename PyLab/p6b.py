
import os
from zipfile import ZipFile

folder = input("Enter folder name that you want to zip : ")

myzip=folder+'.zip'
with ZipFile(myzip,'w') as zip_obj:
    for folder_name,sub_folders,file_names in os.walk(folder):
       for filename in file_names:
           file_path=os.path.join(folder_name,filename)
           zip_obj.write(file_path,os.path.basename(file_path))

if os.path.exists(myzip):
    print("%s zip file created"%myzip)
else:
    print("zip file not created")

