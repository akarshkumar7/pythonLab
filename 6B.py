
import os
from zipfile import ZipFile

foldername=input("enter foldername")
files=os.listdir(foldername)

with ZipFile('x.zip','w')as Z:
    for i in files:
        Z.write(os.path.join(foldername,i))