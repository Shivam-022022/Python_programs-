# Problem Statement:
# Total runs

# Answer:
values = (1, 2, 2, 3, 3, 3, 4, 4, 5)

frequency = {}

for value in values:
    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1

for value, count in frequency.items():
    print(value, ":", count)
