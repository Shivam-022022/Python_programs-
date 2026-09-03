# Duplicate Characters
# Print all duplicate characters in a string.

string = input("Enter a string: ")
duplicates = ""
seen = ""

for ch in string:
    if ch in seen and ch not in duplicates:
        duplicates += ch
    else:
        seen += ch

print("Duplicate characters:", duplicates)
