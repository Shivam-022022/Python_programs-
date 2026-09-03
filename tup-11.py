# Problem Statement:
# Convert a tuple into a list and add a new element.

# Answer:
values = (1, 2, 3, 4)
numbers = list(values)
numbers.append(5)
values = tuple(numbers)
print(values)
