# Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is {'Prime' if is_prime(num) else 'Not Prime'}")
