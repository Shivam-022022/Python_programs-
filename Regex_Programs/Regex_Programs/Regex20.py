import re

text = "Files: report.pdf, photo.jpeg notes.txt archive.tar.gz script.py data-2026.csv"

pattern = r"[\w-]+(?:\.[\w-]+)*\.([A-Za-z0-9]+)(?=[\s,;]|$)"

print("Text:", text)
print("File extensions:", re.findall(pattern, text))
