# Email Validator
# Validate whether a given email address follows a valid format.

email = input("Enter email: ")

if email.count("@") == 1:
    username, domain = email.split("@")
    if username and domain and "." in domain and not domain.startswith(".") and not domain.endswith("."):
        print("Valid email")
    else:
        print("Invalid email")
else:
    print("Invalid email")
