# Read the contents of two text files and create a third file containing
# the contents of both files.

def merge_files(file1, file2, output_file):
    with open(file1, "r") as f1:
        content1 = f1.read()
    with open(file2, "r") as f2:
        content2 = f2.read()

    with open(output_file, "w") as out:
        out.write(content1 + "\n" + content2)

    return content1 + "\n" + content2


if __name__ == "__main__":
    with open("file1.txt", "w") as f:
        f.write("This is the content of file one.")
    with open("file2.txt", "w") as f:
        f.write("This is the content of file two.")

    result = merge_files("file1.txt", "file2.txt", "merged.txt")
    print(result)
