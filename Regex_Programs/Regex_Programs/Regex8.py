import re

text = "Students write programs and use computers in labs on Fridays"

words = re.findall(r"\b\w*s\b", text, re.IGNORECASE)
print("Text:", text)
print("Words ending with s:", words)
