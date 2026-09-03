# Take a list of numbers, use map() and a lambda function to generate a list
# containing their squares.

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))

if __name__ == "__main__":
    print(f"Numbers: {numbers}")
    print(f"Squares: {squares}")
