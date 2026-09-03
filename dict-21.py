# Create a dictionary containing numbers from 1 to 10 as keys and their
# squares as values.

def numbers_and_squares(n=10):
    return {i: i ** 2 for i in range(1, n + 1)}


if __name__ == "__main__":
    result = numbers_and_squares(10)
    print(f"Numbers and their squares: {result}")
