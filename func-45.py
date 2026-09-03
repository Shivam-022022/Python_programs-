# Take a list of words, use filter() and lambda to find words having more than
# five characters.

words = ["cat", "elephant", "dog", "giraffe", "ant", "crocodile"]
long_words = list(filter(lambda w: len(w) > 5, words))

if __name__ == "__main__":
    print(f"Words: {words}")
    print(f"Words with more than 5 characters: {long_words}")
