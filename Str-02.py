# Character Count
# Count the number of vowels, consonants, digits, spaces, and special characters in a given string.

string = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in string:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)
