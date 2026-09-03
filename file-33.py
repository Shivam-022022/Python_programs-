# Create a package texttools containing:
#   a) cleaning.py       -- remove punctuation and extra spaces
#   b) tokenization.py   -- tokenize text
#   c) frequency.py      -- word-frequency analysis
# Create a main program to use the package.
#
# NOTE: A real package would be a "texttools/" directory with
# __init__.py, cleaning.py, tokenization.py, and frequency.py as
# separate files. It is simulated here in one file using clearly
# labelled sections so it matches the file-XX.py naming convention.

import string

# ---------- texttools/cleaning.py ----------
def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))


def remove_extra_spaces(text):
    return " ".join(text.split())
# ---------- end texttools/cleaning.py ----------


# ---------- texttools/tokenization.py ----------
def tokenize(text):
    return text.lower().split()
# ---------- end texttools/tokenization.py ----------


# ---------- texttools/frequency.py ----------
def word_frequency(tokens):
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq
# ---------- end texttools/frequency.py ----------


if __name__ == "__main__":
    text = "Python is great!! Python, is    easy. Python is powerful!"

    cleaned = remove_punctuation(text)
    cleaned = remove_extra_spaces(cleaned)
    print(f"Cleaned Text: {cleaned}")

    tokens = tokenize(cleaned)
    print(f"Tokens: {tokens}")

    freq = word_frequency(tokens)
    print(f"Word Frequency: {freq}")
