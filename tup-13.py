# Problem Statement:
# Modify a tuple by converting it into a list and then back into a tuple.

# Answer:
values = (1, 2, 3, 4)
numbers = list(values)
numbers[1] = 10
values = tuple(numbers)
print(values)
