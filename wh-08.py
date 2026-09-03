limit = int(input("Enter n: "))

first = 0
second = 1

while first <= limit:
    print(first, end=" ")
    next_num = first + second
    first = second
    second = next_num