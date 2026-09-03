# Character Frequency
# Display the frequency of every character in a string.

string = input("Enter a string: ")
frequency = {}

for ch in string:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in frequency:
    print(ch, frequency[ch])
