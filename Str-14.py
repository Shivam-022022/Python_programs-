# Title Case
# Convert the first letter of every word to uppercase.

sentence = input("Enter a sentence: ")
words = sentence.split()
result = []

for word in words:
    if word:
        result.append(word[0].upper() + word[1:])

print(" ".join(result))
