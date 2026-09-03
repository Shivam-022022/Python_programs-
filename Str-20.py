# Count Occurrences of a Word
# Count how many times a specific word appears in a sentence.

sentence = input("Enter a sentence: ")
target = input("Enter word: ")
words = sentence.split()
count = 0

for word in words:
    if word == target:
        count += 1

print("Occurrences:", count)
