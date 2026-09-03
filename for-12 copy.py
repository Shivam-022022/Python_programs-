size = int(input("Enter n: "))

for row in range(1, size + 1):
    for count in range(row):
        print(row, end=" ")
    print()