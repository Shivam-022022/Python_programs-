# Frequency of a Character
# Find the number of times a specified character appears in a string.

string = input("Enter a string: ")
target = input("Enter character: ")
count = 0

for ch in string:
    if ch == target:
        count += 1

print("Frequency:", count)
