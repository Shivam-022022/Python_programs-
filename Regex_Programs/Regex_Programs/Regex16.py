import re

password = input("Enter a password: ")

checks = {
    "at least 8 characters": r".{8,}",
    "an uppercase letter":   r"[A-Z]",
    "a lowercase letter":    r"[a-z]",
    "a digit":               r"\d",
    "a special character":   r"[^A-Za-z0-9\s]",
}

missing = [rule for rule, pat in checks.items() if not re.search(pat, password)]

if not missing:
    print("Strong password: all conditions satisfied.")
else:
    print("Weak password. It must contain:")
    for rule in missing:
        print("  -", rule)

# The same validation in a single pattern using lookaheads:
single = r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9\s]).{8,}"
print("Single-pattern result:", bool(re.fullmatch(single, password)))
