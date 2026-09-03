# Accept a sentence and create a dictionary containing each word and the
# number of times it occurs.

def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        word = word.strip(".,!?;:")
        freq[word] = freq.get(word, 0) + 1
    return freq


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print(f"Word frequency: {word_frequency(sentence)}")
