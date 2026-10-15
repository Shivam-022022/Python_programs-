import re

pattern = r"[6-9]\d{9}"          # Indian mobile numbers start with 6, 7, 8 or 9

number = input("Enter a mobile number: ").strip()

if re.fullmatch(pattern, number):
    print(number, "is a valid 10-digit Indian mobile number.")
else:
    print(number, "is NOT a valid Indian mobile number.")
