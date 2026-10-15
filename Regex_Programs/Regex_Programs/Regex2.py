import re

sentence = input("Enter a sentence: ")

words = re.findall(r"\b[Aa]\w*", sentence)
print("Words beginning with A or a:", words)
