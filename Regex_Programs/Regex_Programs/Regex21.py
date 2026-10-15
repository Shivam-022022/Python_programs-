import re

html = """<html>
<body>
   <h1>Welcome   to   <b>Regex</b> Class!!!</h1>
   <p>Contact:&nbsp;us @ #home... now ***</p>
</body>
</html>"""

text = re.sub(r"<[^>]+>", " ", html)                 # remove HTML tags
text = re.sub(r"&\w+;", " ", text)                   # remove HTML entities such as &nbsp;
text = re.sub(r"[^\w\s.,!?]", "", text)              # remove unwanted punctuation
text = re.sub(r"([.,!?])\1+", r"\1", text)           # collapse repeated punctuation
text = re.sub(r"\s+", " ", text).strip()             # collapse extra whitespace

print("Cleaned text:")
print(text)
