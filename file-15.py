# Read a Python source file and create another file after removing
# single-line comments.

def remove_comments(input_filename, output_filename):
    with open(input_filename, "r") as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines:
        if "#" in line:
            code_part = line.split("#")[0]
            if code_part.strip():
                cleaned_lines.append(code_part.rstrip() + "\n")
        else:
            cleaned_lines.append(line)

    with open(output_filename, "w") as f:
        f.writelines(cleaned_lines)

    return "".join(cleaned_lines)


if __name__ == "__main__":
    with open("source_sample.py", "w") as f:
        f.write("# this is a comment\nx = 5  # inline comment\nprint(x)\n# another comment\n")

    print(remove_comments("source_sample.py", "source_cleaned.py"))
