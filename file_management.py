from pathlib import Path

folder = Path(r"C:\Users\USER\Downloads\IPT_Python_Practice")
folder.mkdir(exist_ok=True)

file_path = folder / "student_notes.txt"
file_new = folder / "user_add.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write("Python File Management Practice.\n")
    file.write("This file contains student activity notes.\n")

print ("File created successfully.")

with open(file_path, 'r', encoding="utf-8") as file:
    content = file.read()
    print ("\nFILE CONTENTS:")
    print (content)

    with open(file_path, "a", encoding="utf-8") as file:
       file.write("New information was added using append mode.\n")

    print("New Information appended")

with open(file_path, "r", encoding="utf-8") as file:
    print ("\nUPDATED FILE CONTENTS:")
    print (file.read())

    print ("===================================================================")
    print ("EXTENSION FINDER")
    extension = input("Enter the extension you are searching for:").strip().lower()
    if extension and not extension.startswith("."):
        extension = "." + extension

        if not extension:
            print ("Please enter an extension.")
        else:
            matches = [
                path for path in folder.rglob("*")
                if path.is_file() and path.suffix.lower() == extension
            ]

            if matches:
                print (f"Files ending in {extension}:")
                for path in matches:
                    print (path)
            else:
                    print(f"No {extension} files found.")



    """ print ("LIST OF FILES AND FOLDERS")
    for item in folder.iterdir():
        if item.is_file():
            print("FILE:", item.name)
        elif item.is_dir():
            print("FOLDER:", item.name)

    print ("\nPYTHON FILES:")
    for file_path in folder.glob("*.py"):
           print(file_path.name)

    print ("\nTEXT FILES:")
    for file_path in folder.rglob("*.txt"):
        print (file_path) """

"""add = input("INPUT A SHORT LETTER TO ADD CONTENT TO user_add.txt:")

with open(file_new, "w", encoding="utf-8") as file:
    file.write(add)

with open(file_new, "r", encoding="utf-8") as file:
        print ("UPDATED MESSAGE MADE BY USER:",file.read())"""
 