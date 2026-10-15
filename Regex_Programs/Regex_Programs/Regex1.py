import re

text = "Order 66 shipped on 15 Oct 2026 to flat 402, Pune 411001."

digits = re.findall(r"\d", text)
numbers = re.findall(r"\d+", text)

print("Text:", text)
print("All digits  :", digits)
print("Whole numbers:", numbers)
