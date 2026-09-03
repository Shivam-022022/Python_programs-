# Remove Duplicate Characters
# Remove duplicate characters while maintaining the original order.

string = input("Enter a string: ")
result = ""

for ch in string:
    if ch not in result:
        result += ch

print(result)
