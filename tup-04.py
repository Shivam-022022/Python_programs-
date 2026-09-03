# Problem Statement:
# Create a tuple of colors. Check whether a given color exists in the tuple

# Answer:
colors = ("red", "blue", "green", "yellow", "black")
color = input("Enter a color: ")
if color in colors:
    print("Color exists")
else:
    print("Color does not exist")
