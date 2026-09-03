# Create a module number_utils.py containing functions to check whether a
# number is prime, palindrome, Armstrong, or perfect. Import the required
# functions into a main program.
#
# NOTE: Combined into a single file. The "number_utils module" section
# below represents what would normally live in number_utils.py.

# ---------- number_utils module ----------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n


def is_perfect(n):
    if n < 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
# ---------- end number_utils module ----------


if __name__ == "__main__":
    num = 153
    print(f"{num} is Prime: {is_prime(num)}")
    print(f"{num} is Palindrome: {is_palindrome(num)}")
    print(f"{num} is Armstrong: {is_armstrong(num)}")

    num2 = 28
    print(f"{num2} is Perfect: {is_perfect(num2)}")
