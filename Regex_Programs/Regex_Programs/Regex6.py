import re

text = "Regular     expressions    are   very      useful"

clean = re.sub(r" {2,}", " ", text)

print("Before:", repr(text))
print("After :", repr(clean))
