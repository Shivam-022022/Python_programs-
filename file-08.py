# Write a program to read a text file and display its lines in reverse
# order.

def reverse_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines[::-1]


if __name__ == "__main__":
    with open("sample.txt", "w") as f:
        f.write("Line one\nLine two\nLine three")

    for line in reverse_lines("sample.txt"):
        print(line.strip())
