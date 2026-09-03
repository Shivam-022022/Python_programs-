# Write a program to count and display the total number of lines present
# in a text file.

def count_lines(filename):
    with open(filename, "r") as f:
        return len(f.readlines())


if __name__ == "__main__":
    with open("sample.txt", "w") as f:
        f.write("Line one\nLine two\nLine three\n")

    print(f"Total number of lines = {count_lines('sample.txt')}")
