import math

number = int(input("Enter number: "))
root = math.isqrt(number)

if root * root != number:
    print("Square root is not an integer")
else:
    flag = True

    if root < 2:
        flag = False

    for divisor in range(2, int(math.sqrt(root)) + 1):
        if root % divisor == 0:
            flag = False
            break

    if flag:
        print("Square root is prime")
    else:
        print("Square root is not prime")