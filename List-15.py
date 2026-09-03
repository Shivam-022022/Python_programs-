# Find the second largest element in a list.

numbers = [25, 48, 12, 75, 63, 91, 54]
largest = numbers[0]
second_largest = None

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number != largest and (second_largest is None or number > second_largest):
        second_largest = number

print("Second largest:", second_largest)
