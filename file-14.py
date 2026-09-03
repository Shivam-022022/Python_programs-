# Read a text file and replace all occurrences of a specified word with
# another word. Save the modified text in the same file or a new file.

def replace_word(input_filename, output_filename, old_word, new_word):
    with open(input_filename, "r") as f:
        content = f.read()
    updated_content = content.replace(old_word, new_word)
    with open(output_filename, "w") as f:
        f.write(updated_content)
    return updated_content


if __name__ == "__main__":
    with open("sample.txt", "w") as f:
        f.write("I like Java. Java is popular. Learning Java is fun.")

    result = replace_word("sample.txt", "sample_updated.txt", "Java", "Python")
    print(result)
