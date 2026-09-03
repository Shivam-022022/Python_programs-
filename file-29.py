# Create a module containing recursive functions for factorial, Fibonacci
# series, sum of digits, and binary conversion. Import and use these
# functions from another program.
#
# NOTE: Combined into a single file. The "recursive_utils module" section
# below represents what would normally live in recursive_utils.py.

# ---------- recursive_utils module ----------
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci_series(n, series=None):
    if series is None:
        series = [0, 1]
    if len(series) >= n:
        return series[:n]
    series.append(series[-1] + series[-2])
    return fibonacci_series(n, series)


def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n < 2:
        return str(n)
    return decimal_to_binary(n // 2) + str(n % 2)
# ---------- end recursive_utils module ----------


if __name__ == "__main__":
    print(f"Factorial of 5: {factorial(5)}")
    print(f"First 8 Fibonacci numbers: {fibonacci_series(8)}")
    print(f"Sum of digits of 12345: {sum_of_digits(12345)}")
    print(f"Binary of 42: {decimal_to_binary(42)}")
