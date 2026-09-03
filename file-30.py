# Create a package named mathutils containing:
#   a) basic.py       -- arithmetic operations
#   b) number.py      -- prime, Armstrong, palindrome functions
#   c) statistics.py  -- mean, maximum, minimum
# Create a main program that imports functions from each module.
#
# NOTE: A real package would be a "mathutils/" directory with
# __init__.py, basic.py, number.py, and statistics.py as separate files.
# It is simulated here in one file using clearly labelled sections so it
# matches the file-XX.py naming convention; each section below is what
# would be its own module inside the mathutils package.

# ---------- mathutils/basic.py ----------
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"
# ---------- end mathutils/basic.py ----------


# ---------- mathutils/number.py ----------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == n


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
# ---------- end mathutils/number.py ----------


# ---------- mathutils/statistics.py ----------
def mean(numbers):
    return sum(numbers) / len(numbers)


def maximum(numbers):
    return max(numbers)


def minimum(numbers):
    return min(numbers)
# ---------- end mathutils/statistics.py ----------


if __name__ == "__main__":
    print(f"Add: {add(10, 5)}")
    print(f"Is 29 Prime: {is_prime(29)}")
    print(f"Is 153 Armstrong: {is_armstrong(153)}")

    nums = [12, 45, 3, 89, 34]
    print(f"Mean: {mean(nums):.2f}, Max: {maximum(nums)}, Min: {minimum(nums)}")
