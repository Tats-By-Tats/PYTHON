from pathlib import Path
import os

file_path = Path (r"C:\Users\USER\Downloads\IPT_Python_Practice") / "student_notes.txt"

if file_path.exists():

    print ("FILE PERMISSION REPORT")
    print ("--------------------------------------------------------------")

    print ("Readable:", "The process is readable" if os.access(file_path, os.R_OK) else "The read permission is denied")
    print ("Writable:", "The process is writable" if os.access(file_path, os.W_OK) else "The write permission is denied ")
    print ("Executable:","The process is executable" if os.access(file_path, os.X_OK) else "The execute permission is denied")
else:
    print ("File not found.")