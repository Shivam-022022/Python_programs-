# Problem Statement:
# Calculate the average of elements stored in a tuple.

# Answer:
numbers = (10, 20, 30, 40, 50)
total = 0

for number in numbers:
    total += number

average = total / len(numbers)
print(average)
