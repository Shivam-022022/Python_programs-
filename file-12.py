# Read a text file and count how many times each word occurs. Display the
# result using a dictionary.

def word_frequency(filename):
    with open(filename, "r") as f:
        content = f.read().lower()
    words = content.split()
    freq = {}
    for word in words:
        word = word.strip(".,!?;:")
        freq[word] = freq.get(word, 0) + 1
    return freq


if __name__ == "__main__":
    with open("sample.txt", "w") as f:
        f.write("python is easy. python is powerful. python is popular.")

    freq = word_frequency("sample.txt")
    for word, count in freq.items():
        print(f"{word}: {count}")
