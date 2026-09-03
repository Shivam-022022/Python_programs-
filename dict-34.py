# Take a string, use a dictionary to find the first character that occurs
# more than once.

def first_repeated_character(s):
    seen = {}
    for ch in s:
        if ch in seen:
            return ch
        seen[ch] = 1
    return None


if __name__ == "__main__":
    text = "programming"
    print(f"String: {text}")
    print(f"First repeated character: {first_repeated_character(text)}")
