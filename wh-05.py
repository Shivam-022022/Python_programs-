limit = int(input("Enter n: "))

num = 1
total = 0

while num <= limit:
    total += num
    num += 2

print(total)