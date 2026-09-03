# Write a program using functions, map(), filter(), and lambda expressions to
# process a list of words and:
# - Find the length of every word.
# - Extract words having more than five characters.
# - Sort words according to their length.

words = ["python", "code", "function", "map", "lambda", "filter", "loop"]


def word_lengths(word_list):
    return list(map(lambda w: (w, len(w)), word_list))


def long_words(word_list):
    return list(filter(lambda w: len(w) > 5, word_list))


def sort_by_length(word_list):
    return sorted(word_list, key=lambda w: len(w))


if __name__ == "__main__":
    print(f"Words: {words}")

    lengths = word_lengths(words)
    print(f"Word lengths: {lengths}")

    filtered = long_words(words)
    print(f"Words with more than 5 characters: {filtered}")

    sorted_words = sort_by_length(words)
    print(f"Sorted by length: {sorted_words}")
