# Create separate functions for addition, subtraction, multiplication, and
# division. Pass these functions as arguments to another function called
# calculate().

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def calculate(operation, a, b):
    return operation(a, b)


if __name__ == "__main__":
    x, y = 10, 5
    print(f"Addition: {calculate(add, x, y)}")
    print(f"Subtraction: {calculate(subtract, x, y)}")
    print(f"Multiplication: {calculate(multiply, x, y)}")
    print(f"Division: {calculate(divide, x, y)}")
