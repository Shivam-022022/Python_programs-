# Create a lambda function to calculate simple interest using principal, rate,
# and time.

simple_interest = lambda p, r, t: (p * r * t) / 100

if __name__ == "__main__":
    p, r, t = 10000, 5, 2
    print(f"Simple Interest = {simple_interest(p, r, t)}")
