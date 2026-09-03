# Second Most Frequent Character
# Find the second most frequently occurring character.

string = input("Enter a string: ")
frequency = {}

for ch in string:
    frequency[ch] = frequency.get(ch, 0) + 1

if len(frequency) >= 2:
    characters = sorted(frequency, key=frequency.get, reverse=True)
    second = characters[1]
    print("Second most frequent character:", second)
    print("Frequency:", frequency[second])
else:
    print("Not enough distinct characters")
