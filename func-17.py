# Write a function that accepts n and returns the first n Fibonacci numbers.

def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list


if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(f"First {n} Fibonacci numbers: {fibonacci(n)}")
