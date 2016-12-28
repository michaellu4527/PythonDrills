import os
import shutil


source = ("C:/Users/Student/Desktop/Folder A")
dest = ("C:/Users/Student/Desktop/Folder B")

#86400 seconds in 24 hours

def fileMover(src, dst):
    files = os.listdir(src)
    for file_name in files:
        if file_name.endswith('.txt'):
            abs_path1 = os.path.join(src, file_name)
            shutil.move(abs_path1, dst)
            print ("Moved file")

            abs_path2 = os.path.join(file_name, dst)
            print os.path.abspath(abs_path2)

fileMover(source,dest)
