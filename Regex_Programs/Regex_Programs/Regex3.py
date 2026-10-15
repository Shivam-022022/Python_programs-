import re
from collections import Counter

text = "Regular expressions make text processing easy and powerful"

vowels = re.findall(r"[aeiou]", text, re.IGNORECASE)

print("Text:", text)
print("Total vowels:", len(vowels))
print("Count of each vowel:", dict(Counter(v.lower() for v in vowels)))
