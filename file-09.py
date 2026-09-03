# Read a text file and count the number of vowels and consonants present
# in the file.

def count_vowels_consonants(filename):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    with open(filename, "r") as f:
        content = f.read()
    for ch in content:
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count


if __name__ == "__main__":
    with open("sample.txt", "w") as f:
        f.write("Hello World, this is Python programming.")

    vowels, consonants = count_vowels_consonants("sample.txt")
    print(f"Vowels = {vowels}, Consonants = {consonants}")
