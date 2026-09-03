# Read a text file and find the longest word present in the file.

def longest_word(filename):
    with open(filename, "r") as f:
        content = f.read()
    words = content.split()
    return max(words, key=len) if words else ""


if __name__ == "__main__":
    with open("sample.txt", "w") as f:
        f.write("Python programming is extremely interesting and educational.")

    print(f"Longest word = {longest_word('sample.txt')}")
