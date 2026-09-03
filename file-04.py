# Write a program to read a text file line by line and display each line
# separately.

def read_lines(filename):
    with open(filename, "r") as f:
        return f.readlines()


if __name__ == "__main__":
    with open("sample.txt", "w") as f:
        f.write("Line one\nLine two\nLine three")

    for i, line in enumerate(read_lines("sample.txt"), start=1):
        print(f"Line {i}: {line.strip()}")
