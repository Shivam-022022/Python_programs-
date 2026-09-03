# Read a text file and create another file containing the same text in
# uppercase.

def convert_to_uppercase(input_filename, output_filename):
    with open(input_filename, "r") as f:
        content = f.read()
    upper_content = content.upper()
    with open(output_filename, "w") as f:
        f.write(upper_content)
    return upper_content


if __name__ == "__main__":
    with open("sample.txt", "w") as f:
        f.write("this text will be converted to uppercase.")

    print(convert_to_uppercase("sample.txt", "sample_upper.txt"))
