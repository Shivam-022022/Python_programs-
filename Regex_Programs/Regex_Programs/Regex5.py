import re

text = "Name:\tAarav Sharma\nCity: Pune\nCourse:\tPython  Programming"

spaces = re.findall(r" ", text)
tabs = re.findall(r"\t", text)
newlines = re.findall(r"\n", text)

print("Text (repr):", repr(text))
print("Spaces   :", len(spaces))
print("Tabs     :", len(tabs))
print("Newlines :", len(newlines))

# Positions of each whitespace character
for m in re.finditer(r"[ \t\n]", text):
    kind = {" ": "space", "\t": "tab", "\n": "newline"}[m.group()]
    print(f"  {kind} at index {m.start()}")
