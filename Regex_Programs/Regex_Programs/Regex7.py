import re

sentence = input("Enter a sentence: ")

words = re.findall(r"\b\w{5}\b", sentence)
print("Words with exactly five characters:", words)
