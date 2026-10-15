import re

text = ("Visit https://www.python.org/downloads/ or http://example.com/page?id=5. "
        "Not a link: www.google.com and ftp://files.example.com")

urls = [u.rstrip(".,;:!?)") for u in re.findall(r"https?://[^\s<>\"']+", text)]
print("Web addresses found:")
for u in urls:
    print(" ", u)
