# Take a list of words, create a dictionary where the key is the word
# length and the value is a list of words having that length.

def group_words_by_length(words):
    grouped = {}
    for word in words:
        grouped.setdefault(len(word), []).append(word)
    return grouped


if __name__ == "__main__":
    words = ["cat", "dog", "fish", "lion", "ant", "tiger", "owl"]
    print(f"Words: {words}")
    print(f"Grouped by length: {group_words_by_length(words)}")
