import os
import shutil
import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class fileTransfer:

    def __init__(self, master):
        # ==================================== Header Content =========================================#
        # Set title of GUI
        master.title('Easy File Transfer')
        master.resizable(False, False)      # Make window unable to change in size

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack(fill=BOTH)   # Expands vertically and horizontally

        # Header text
        ttk.Label(self.frame_header, text="Easy File Transfer Application", font="Times 16 bold").pack()

        self.frame_desc = ttk.Frame(master)
        self.frame_desc.pack(fill=BOTH)

        # Short description, describing how to use the GUI to the user.
        ttk.Label(self.frame_desc, text=("First, select source and destination folders. Then, click 'Move Files' "
                                           "to move files that have been modified in the last 24 hours. ")).pack(padx=12, pady=15)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack(fill=BOTH)

        #======================================== Buttons ============================================#
        ttk.Button(self.frame_content, text="Browse...",
                   command=lambda: self.getSource()).grid(row=0, column=0, padx=10, pady=10, sticky=W)

        ttk.Button(self.frame_content, text="Browse...",
                   command=lambda: self.getDest()).grid(row=1, column=0, padx=10, pady=10, sticky=W)

        ttk.Button(self.frame_content, text="Move Files",
                   command=lambda: self.moveFiles()).grid(row=2, column=1, columnspan=2, padx=10, pady=10)


        # ================================= Button Labels ============================================#
        ttk.Label(self.frame_content, text="Source Folder:").grid(row=0, column=1, padx=10, pady=3)
        self.src_text = StringVar()
        self.entry_src = ttk.Entry(self.frame_content, width=60, textvariable=self.src_text)
        self.entry_src.grid(row=0, column=2, padx=10, pady=3, sticky=W+E)
        self.entry_src.configure(state='readonly')

        ttk.Label(self.frame_content, text="Destination Folder:").grid(row=1, column=1, padx=10, pady=3)
        self.dest_text= StringVar()
        self.entry_dest = ttk.Entry(self.frame_content, width=60, textvariable=self.dest_text)
        self.entry_dest.grid(row=1, column=2, padx=10, pady=3, sticky=W+E)
        self.entry_dest.configure(state='readonly')


    # ================================= Functions ============================================#
    def getSource(self):
        srcDirName = filedialog.askdirectory()
        self.src_text.set(srcDirName + '/')

    def getDest(self):
        dstDirName = filedialog.askdirectory()
        self.dest_text.set(dstDirName + '/')

    # Function will move any files from the specified source to destination folder modified within the last 24 hours.
    def moveFiles(self):
        src = self.src_text.get()
        dst = self.dest_text.get()
        files = os.listdir(src)
        count = 0

        for file_name in files:  # Cycles through directory of files
            abs_path1 = os.path.join(src, file_name)
            mod_time = os.path.getmtime(abs_path1)  # Gets time since last modification of file
            check_time = time.time() - 86400  # Calculates time that was 24 hours prior

            if mod_time >= check_time:  # File has been modified if it passes this check
                abs_path3 = os.path.join(src, file_name)
                shutil.move(abs_path3, dst)  # Moves file to new location

                messagebox.showinfo("File Transfer", "Operation successful! \n\nFiles that have been modified in the last 24 hours have been moved.")
                count += 1  # Increments a counter to indicate a file has been moved

        if count == 0:  # No files have been moved, so print out message
            messagebox.showwarning("File Transfer", "Sorry, no files have been modified in the last 24 hours...")

def main():
    root = Tk ()
    file_transfer = fileTransfer(root)
    root.mainloop()

if __name__ == "__main__": main()
