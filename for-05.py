count = int(input("Enter n: "))

factorial = 1
total = 1

for value in range(1, count + 1):
    factorial = factorial * value
    total = total + 1 / factorial

print(total)