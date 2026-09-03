# Uppercase and Lowercase Count
# Count the number of uppercase and lowercase letters in a string.

string = input("Enter a string: ")
uppercase = 0
lowercase = 0

for ch in string:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
