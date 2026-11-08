from pathlib import Path
from datetime import datetime
import csv

folder = Path(r"C:\Users\USER\Downloads\IPT_Python_Practice")
report_path = folder / "file_report.csv"
report_count = 0

with open (report_path, "w", newline="", encoding="utf-8") as csv_file:

    writer = csv.writer(csv_file)

    writer.writerow([
        "Filename",
        "Extension", 
        "Size (bytes)", 
        "Last Modified"
    ])

    for file_path in folder.iterdir():
        if file_path.is_file() and file_path != report_path:
            details = file_path.stat()
            report_count += 1


            modified = datetime.fromtimestamp(details.st_mtime)
            writer.writerow([
                file_path.name,
                file_path.suffix.lower() or "No extension",
                details.st_size,
                modified.strftime("%Y-%m-%d" "  %H:%M:%S")
            ])

print ("Report saved to:", report_path.resolve())
print ("Total number of files included in the report: ", report_count)