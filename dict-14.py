# Accept a string from the user and create a dictionary containing each
# character and its frequency.

def character_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


if __name__ == "__main__":
    text = input("Enter a string: ")
    print(f"Character frequency: {character_frequency(text)}")
