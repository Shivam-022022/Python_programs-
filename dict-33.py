# Take a string, use a dictionary to find the first character that occurs
# only once.

def first_unique_character(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None


if __name__ == "__main__":
    text = "swiss"
    print(f"String: {text}")
    print(f"First unique character: {first_unique_character(text)}")
