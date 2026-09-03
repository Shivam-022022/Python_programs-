# Password Validator
# Validate a password based on these conditions:
# Minimum 8 characters
# At least one uppercase letter
# One lowercase letter
# One digit
# One special character

password = input("Enter password: ")
uppercase = False
lowercase = False
digit = False
special = False

for ch in password:
    if ch.isupper():
        uppercase = True
    elif ch.islower():
        lowercase = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and uppercase and lowercase and digit and special:
    print("Valid password")
else:
    print("Invalid password")
