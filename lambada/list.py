words = ["apple", "banana", "cat", "computer", "python", "book"]


# a) Find length of every word
lengths = list(
    map(lambda word: len(word), words)
)

print("Lengths =", lengths)


# b) Words having more than 5 characters
long_words = list(
    filter(lambda word: len(word) > 5, words)
)

print("Words having more than 5 characters:")
print(long_words)


# c) Sort words according to length
sorted_words = sorted(
    words,
    key=lambda word: len(word)
)

print("Words sorted by length:")
print(sorted_words)