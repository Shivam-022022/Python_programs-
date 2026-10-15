import re

text = "Python Was Created By Guido van Rossum In 1991 At CWI"

uppercase = re.findall(r"[A-Z]", text)
print("Text:", text)
print("Uppercase letters:", uppercase)
print("Count:", len(uppercase))
