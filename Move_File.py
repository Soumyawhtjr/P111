import os
import shutil
from_dir='C:/Users/dell/Downloads'
to_dir="C:/Users/dell/Documents/docs"
list_of_files=os.listdir(from_dir)
###print(list_of_files)
for i in list_of_files:
    root,extension=os.path.splitext(i)
    print("Root:",root,"Ext:",extension)
