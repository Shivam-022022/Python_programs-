import re

sentence = "This is is a test of the the repeated Repeated words in in a sentence"

matches = re.findall(r"\b(\w+)\s+\1\b", sentence, re.IGNORECASE)
print("Sentence:", sentence)
print("Consecutive repeated words:", matches)

# Optionally fix the sentence by removing the duplicates
fixed = re.sub(r"\b(\w+)(\s+\1\b)+", r"\1", sentence, flags=re.IGNORECASE)
print("After removing duplicates:", fixed)
