# Count the frequency of each element in a list.

numbers = list(map(int, input("Enter list elements: ").split()))
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

for number in frequency:
    print(number, ":", frequency[number])
