x = float(input("Enter x: "))
terms = int(input("Enter n: "))

answer = 0
fact = 1

for value in range(terms + 1):
    if value > 0:
        fact = fact * value
    if value % 2 == 0:
        answer = answer + ((-1) ** (value // 2)) * (x ** value) / fact

print(answer)