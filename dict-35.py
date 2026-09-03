# Accept a paragraph and create a dictionary where:
# - Key = word length
# - Value = number of words having that length

def word_length_frequency(paragraph):
    freq = {}
    words = paragraph.split()
    for word in words:
        cleaned = word.strip(".,!?;:")
        length = len(cleaned)
        freq[length] = freq.get(length, 0) + 1
    return freq


if __name__ == "__main__":
    paragraph = input("Enter a paragraph: ")
    print(f"Word length frequency: {word_length_frequency(paragraph)}")
