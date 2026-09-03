size = int(input("Enter n: "))

for row in range(1, size + 1):
    for letter in range(row):
        print(chr(65 + letter), end=" ")
    print()