# Write a program to open a text file and display its complete contents.

def display_file_contents(filename):
    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    # create a sample file first so this script is runnable standalone
    with open("sample.txt", "w") as f:
        f.write("Hello World\nThis is a sample file.\nPython file handling demo.")

    print(display_file_contents("sample.txt"))
