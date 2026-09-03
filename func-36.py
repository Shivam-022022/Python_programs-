# Use a lambda function to find the maximum of two numbers.

maximum = lambda a, b: a if a > b else b

if __name__ == "__main__":
    x, y = 15, 27
    print(f"Maximum of {x} and {y} = {maximum(x, y)}")
