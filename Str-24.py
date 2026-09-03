# Most Frequent Character
# Find the character with the highest frequency.

string = input("Enter a string: ")
frequency = {}

for ch in string:
    frequency[ch] = frequency.get(ch, 0) + 1

if frequency:
    most_frequent = max(frequency, key=frequency.get)
    print("Most frequent character:", most_frequent)
    print("Frequency:", frequency[most_frequent])
else:
    print("String is empty")
