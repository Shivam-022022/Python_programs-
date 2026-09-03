# Take a list of words; sort them according to their length using lambda.

words = ["banana", "kiwi", "apple", "fig", "watermelon"]
sorted_words = sorted(words, key=lambda w: len(w))

if __name__ == "__main__":
    print(f"Words: {words}")
    print(f"Sorted by length: {sorted_words}")
