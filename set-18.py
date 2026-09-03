# Accept a sentence from the user and use a set to display all unique
# words.

def unique_words(sentence):
    return set(sentence.lower().split())


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print(f"Unique words: {unique_words(sentence)}")
