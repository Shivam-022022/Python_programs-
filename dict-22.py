# Create a dictionary containing numbers from 1 to 20 as keys and their
# squares as values, but include only even numbers.

def even_numbers_and_squares(n=20):
    return {i: i ** 2 for i in range(1, n + 1) if i % 2 == 0}


if __name__ == "__main__":
    result = even_numbers_and_squares(20)
    print(f"Even numbers and their squares: {result}")
