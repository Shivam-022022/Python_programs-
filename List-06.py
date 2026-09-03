# Write a program to find the largest and smallest number in a list without using max() or min().

numbers = [25, 12, 48, 7, 36, 19]
largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print("Largest:", largest)
print("Smallest:", smallest)
