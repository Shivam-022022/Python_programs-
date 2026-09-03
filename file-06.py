# Write a program to count the total number of words present in a text
# file.

def count_words(filename):
    with open(filename, "r") as f:
        content = f.read()
    return len(content.split())


if __name__ == "__main__":
    with open("sample.txt", "w") as f:
        f.write("This is a sample text file with some words.")

    print(f"Total number of words = {count_words('sample.txt')}")
