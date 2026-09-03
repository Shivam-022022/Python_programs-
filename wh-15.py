count = int(input("How many numbers: "))

largest = None
i = 1

while i <= count:
    number = int(input("Enter number: "))

    if largest is None or number > largest:
        largest = number

    i += 1

print(largest)