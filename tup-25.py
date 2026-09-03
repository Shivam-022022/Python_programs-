# Problem Statement:
# Highest-priced item
# Lowest-priced item
# Store temperatures of seven days in a tuple and determine:
# Maximum temperature
# Minimum temperature

# Answer:
runs = (45, 78, 32, 90, 56, 100, 67, 23, 81, 54)

total = sum(runs)
highest = runs[0]
lowest = runs[0]

for score in runs:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score

average = total / len(runs)

print("Total runs:", total)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average score:", average)
