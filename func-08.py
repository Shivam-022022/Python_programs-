# Create a function power(base, exponent) to calculate the value of base raised to exponent.

def power(base, exponent):
    return base ** exponent


if __name__ == "__main__":
    b = float(input("Enter base: "))
    e = float(input("Enter exponent: "))
    print(f"{b} ^ {e} = {power(b, e)}")
