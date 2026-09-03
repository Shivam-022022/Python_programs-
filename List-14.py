# Create a list containing duplicate values and display only unique elements.

numbers = [10, 20, 10, 30, 20, 40, 30, 50]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)
