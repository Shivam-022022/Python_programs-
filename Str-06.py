# Replace Characters
# Replace all occurrences of a given character with another character.

string = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter replacement character: ")
result = ""

for ch in string:
    if ch == old:
        result += new
    else:
        result += ch

print(result)
