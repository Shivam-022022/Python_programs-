import re

# Pattern: 3 uppercase letters - 4 digits - 2 uppercase letters  (ABC-1234-XY)
pattern = r"[A-Z]{3}-\d{4}-[A-Z]{2}"

code = input("Enter product code (format ABC-1234-XY): ").strip()

if re.fullmatch(pattern, code):
    print(code, "is a valid product code.")
else:
    print(code, "is NOT a valid product code.")
