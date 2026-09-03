# Problem Statement:
# Find the largest and smallest number in a tuple without using max() and min().

# Answer:
numbers = (45, 12, 78, 23, 89, 34, 56)
largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print("Largest:", largest)
print("Smallest:", smallest)
