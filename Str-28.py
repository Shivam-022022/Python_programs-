# Word Frequency Dictionary
# Count the frequency of every word in a paragraph.

paragraph = input("Enter paragraph: ")
words = paragraph.lower().split()
frequency = {}

for word in words:
    word = word.strip(".,!?;:"'()[]{}")
    if word:
        frequency[word] = frequency.get(word, 0) + 1

for word in frequency:
    print(word, frequency[word])
