# Take a list of integers, use filter() with an appropriate lambda expression
# to identify prime numbers.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


numbers = [10, 11, 12, 13, 14, 15, 17, 18, 19]
primes = list(filter(lambda x: is_prime(x), numbers))

if __name__ == "__main__":
    print(f"Numbers: {numbers}")
    print(f"Prime Numbers: {primes}")
