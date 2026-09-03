size = int(input("Enter n: "))

for row in range(1, size + 1):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()