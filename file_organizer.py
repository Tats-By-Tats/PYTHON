from pathlib import Path
import shutil

moved_count = 0
skipped_count = 0

source_folder = Path(r"C:\Users\USER\Downloads\IPT_Python_Practice") / "To_Organize"
for file_path in source_folder.iterdir():
    if file_path.is_file():
        extension = file_path.suffix.lower()
        
        if extension:
            folder_name = extension[1:].upper()
        else:
            folder_name = "NO_EXTENSION"

        destination_folder = source_folder / folder_name
        destination_folder.mkdir(exist_ok=True)

        destination_file = destination_folder / file_path.name

        if destination_file.exists():
            print ("Skipped:", file_path.name)
            skipped_count +=1
            continue

        shutil.move(str(file_path), str(destination_file))
        print ("Moved:", file_path.name, "to", folder_name)
        moved_count +=1

print ("Moved Files:", moved_count)
print ("Skipped Files:", skipped_count)
print ("\nFILE ORGANIZATION COMPLETED.")
