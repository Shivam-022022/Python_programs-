import re

text = "Hello, World! Python@3.12 costs $0 #free & fun :)"

clean = re.sub(r"[^A-Za-z0-9 ]", "", text)

print("Original:", text)
print("Cleaned :", clean)
