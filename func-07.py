# Write a function that accepts n and returns the sum of the first n natural numbers.

def sum_natural_numbers(n):
    return n * (n + 1) // 2


if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(f"Sum of first {n} natural numbers = {sum_natural_numbers(n)}")
