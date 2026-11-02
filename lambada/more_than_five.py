words = ["apple", "banana", "cat", "computer", "book", "python"]

result = list(filter(lambda word: len(word) > 5, words))

print("Words =", result)