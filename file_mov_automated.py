import os
import shutil
import time

source = ("C:/Users/Student/Desktop/Folder A")
dest = ("C:/Users/Student/Desktop/Folder B")

# 86400 seconds in 24 hours

# This function will automatically move files from one folder to another that have been modified
# within the last 24 hours. 
def fileMover(src, dst):
    files = os.listdir(src)
    count = 0

    for file_name in files:     # Cycles through directory of files
        abs_path1 = os.path.join(src, file_name)
        mod_time = os.path.getmtime(abs_path1)  # Gets time since last modification of file
        check_time =  time.time() - 86400        # Calculates time that was 24 hours prior

        if mod_time >= check_time:       # File has been modified if it passes this check
            abs_path3 = os.path.join(src, file_name)
            shutil.move(abs_path3, dst)     # Moves file to new location

            abs_path2 = os.path.join(file_name, dst)
            mov_loc = os.path.abspath(abs_path2)
            print (file_name + " has been moved to: " + mov_loc )
            count += 1      # Increments a counter to indicate a file has been moved

    if count == 0:      # No files have been moved, so print out message
        print ("No files have been modified in the last 24 hours. ")

fileMover(source,dest)