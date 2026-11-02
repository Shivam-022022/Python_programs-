words = ["apple", "cat", "banana", "dog", "computer"]

result = sorted(words, key=lambda word: len(word))

print("Sorted words =", result)