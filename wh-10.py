number = int(input("Enter number: "))

divisor = 2
prime = True

if number < 2:
    prime = False

while divisor <= number // 2:
    if number % divisor == 0:
        prime = False
        break
    divisor += 1

if prime:
    print("Prime")
else:
    print("Not Prime")