import re

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"

email = input("Enter an email address: ").strip()

if re.fullmatch(pattern, email):
    print(email, "has a valid email format.")
else:
    print(email, "does NOT look like a valid email address.")
