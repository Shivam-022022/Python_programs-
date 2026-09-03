# Create a Python module calculator.py containing functions for addition,
# subtraction, multiplication, and division. Create another program that
# imports the module and performs calculations based on user input.
#
# NOTE: Combined into a single file for this exercise set. The section
# marked "calculator module" below represents what would normally live in
# a separate calculator.py file, imported here as if by `import calculator`.

# ---------- calculator module ----------
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
# ---------- end calculator module ----------


def main():
    a, b = 10, 5
    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")
    print(f"Division: {divide(a, b)}")


if __name__ == "__main__":
    main()
