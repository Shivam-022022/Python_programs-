# Accept a word from the user and search for it in a text file. Display
# the number of occurrences and the line numbers where it appears.

def search_word(filename, search_term):
    occurrences = 0
    line_numbers = []
    with open(filename, "r") as f:
        for i, line in enumerate(f, start=1):
            count_in_line = line.lower().split().count(search_term.lower())
            if search_term.lower() in line.lower():
                occurrences += line.lower().count(search_term.lower())
                line_numbers.append(i)
    return occurrences, line_numbers


if __name__ == "__main__":
    with open("sample.txt", "w") as f:
        f.write("Python is great.\nI love Python.\nPython is easy to learn.")

    word = "Python"
    occurrences, line_numbers = search_word("sample.txt", word)
    print(f"'{word}' occurs {occurrences} times")
    print(f"Found on lines: {line_numbers}")
