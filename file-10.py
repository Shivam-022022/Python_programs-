# Read a text file and calculate the number of alphabets, digits, spaces,
# and special characters.

def analyze_characters(filename):
    alphabets = digits = spaces = special = 0
    with open(filename, "r") as f:
        content = f.read()
    for ch in content:
        if ch.isalpha():
            alphabets += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1
        else:
            special += 1
    return alphabets, digits, spaces, special


if __name__ == "__main__":
    with open("sample.txt", "w") as f:
        f.write("Roll No 101, Marks: 85% (Grade A)")

    alphabets, digits, spaces, special = analyze_characters("sample.txt")
    print(f"Alphabets = {alphabets}")
    print(f"Digits = {digits}")
    print(f"Spaces = {spaces}")
    print(f"Special Characters = {special}")
