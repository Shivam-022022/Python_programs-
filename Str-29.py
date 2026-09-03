# Sentence Reversal
# Reverse the order of words in a sentence without changing the words themselves.
# Example: Input: Python is easy Output: easy is Python

sentence = input("Enter a sentence: ")
words = sentence.split()
result = ""

for i in range(len(words) - 1, -1, -1):
    result += words[i]
    if i != 0:
        result += " "

print(result)
