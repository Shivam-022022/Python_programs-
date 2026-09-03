# Substring Search
# Check whether a given substring exists in the main string.

string = input("Enter main string: ")
substring = input("Enter substring: ")

if substring in string:
    print("Substring exists")
else:
    print("Substring does not exist")
