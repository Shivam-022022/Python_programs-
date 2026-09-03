number = int(input("Enter number: "))

fact = 1
count = 1

while count <= number:
    fact *= count
    count += 1

print(fact)