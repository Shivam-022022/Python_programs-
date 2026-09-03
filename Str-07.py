# Remove Spaces
# Remove all spaces from the input string.

string = input("Enter a string: ")
result = ""

for ch in string:
    if ch != " ":
        result += ch

print(result)
