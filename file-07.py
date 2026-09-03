# Write a program to count the total number of characters in a text file,
# including spaces.

def count_characters(filename):
    with open(filename, "r") as f:
        content = f.read()
    return len(content)


if __name__ == "__main__":
    with open("sample.txt", "w") as f:
        f.write("Hello World")

    print(f"Total number of characters = {count_characters('sample.txt')}")
