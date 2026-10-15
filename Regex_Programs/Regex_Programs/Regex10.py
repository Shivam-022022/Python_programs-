import re

sentence = "Regular expressions aren't hard once you practise a little."

words = re.findall(r"[A-Za-z0-9']+", sentence)
print("Sentence:", sentence)
print("Words:", words)
print("Number of words:", len(words))
