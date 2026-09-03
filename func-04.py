# Create a function simple_interest(p, r, t) to calculate simple interest.

def simple_interest(p, r, t):
    return (p * r * t) / 100


if __name__ == "__main__":
    p = float(input("Enter principal: "))
    r = float(input("Enter rate of interest: "))
    t = float(input("Enter time (years): "))
    print(f"Simple Interest = {simple_interest(p, r, t)}")
