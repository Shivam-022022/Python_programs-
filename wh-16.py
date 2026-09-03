count = int(input("How many numbers: "))

smallest = None
i = 1

while i <= count:
    number = int(input("Enter number: "))

    if smallest is None or number < smallest:
        smallest = number

    i += 1

print(smallest)