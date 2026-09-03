# Create a module string_utils.py containing functions to count vowels,
# reverse a string, check palindrome, count words, and remove spaces.
#
# NOTE: Combined into a single file. The "string_utils module" section
# below represents what would normally live in string_utils.py.

# ---------- string_utils module ----------
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)


def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_words(s):
    return len(s.split())


def remove_spaces(s):
    return s.replace(" ", "")
# ---------- end string_utils module ----------


if __name__ == "__main__":
    text = "Madam Arora teaches malayalam"
    print(f"Vowels: {count_vowels(text)}")
    print(f"Reversed: {reverse_string(text)}")
    print(f"Is Palindrome: {is_palindrome(text)}")
    print(f"Word Count: {count_words(text)}")
    print(f"No Spaces: {remove_spaces(text)}")
