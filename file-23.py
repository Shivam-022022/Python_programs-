# Write a program to compare two text files and display whether their
# contents are identical. If different, identify the first line where they
# differ.

def compare_files(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    max_lines = max(len(lines1), len(lines2))
    for i in range(max_lines):
        line1 = lines1[i] if i < len(lines1) else None
        line2 = lines2[i] if i < len(lines2) else None
        if line1 != line2:
            return False, i + 1
    return True, None


if __name__ == "__main__":
    with open("fileA.txt", "w") as f:
        f.write("Line one\nLine two\nLine three")
    with open("fileB.txt", "w") as f:
        f.write("Line one\nLine TWO\nLine three")

    identical, diff_line = compare_files("fileA.txt", "fileB.txt")
    if identical:
        print("Files are identical")
    else:
        print(f"Files differ starting at line {diff_line}")
