# Define a function that accepts two numbers and returns the greater number.

def greater_number(a, b):
    return a if a > b else b


if __name__ == "__main__":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(f"The greater number is {greater_number(x, y)}")
