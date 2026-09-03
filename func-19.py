# Write a function that accepts the number of units consumed and calculates the
# electricity bill according to predefined slabs.

def electricity_bill(units):
    if units <= 100:
        cost = units * 3.0
    elif units <= 200:
        cost = 100 * 3.0 + (units - 100) * 4.5
    elif units <= 300:
        cost = 100 * 3.0 + 100 * 4.5 + (units - 200) * 6.0
    else:
        cost = 100 * 3.0 + 100 * 4.5 + 100 * 6.0 + (units - 300) * 7.0
    return cost


if __name__ == "__main__":
    units = float(input("Enter units consumed: "))
    print(f"Electricity bill = Rs. {electricity_bill(units):.2f}")
