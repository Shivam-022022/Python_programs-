# Develop a modular program using functions to calculate electricity bills using
# different consumption slabs. Include fixed charges, taxes, and discounts.

FIXED_CHARGE = 50
TAX_RATE = 0.05
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.02


def slab_cost(units):
    if units <= 100:
        return units * 3.0
    elif units <= 200:
        return 100 * 3.0 + (units - 100) * 4.5
    elif units <= 300:
        return 100 * 3.0 + 100 * 4.5 + (units - 200) * 6.0
    else:
        return 100 * 3.0 + 100 * 4.5 + 100 * 6.0 + (units - 300) * 7.0


def apply_tax(amount):
    return amount * TAX_RATE


def apply_discount(units, amount):
    if units > DISCOUNT_THRESHOLD:
        return amount * DISCOUNT_RATE
    return 0


def calculate_bill(units):
    base = slab_cost(units)
    tax = apply_tax(base)
    discount = apply_discount(units, base)
    total = FIXED_CHARGE + base + tax - discount
    return {
        "base": base,
        "tax": tax,
        "discount": discount,
        "fixed_charge": FIXED_CHARGE,
        "total": total,
    }


if __name__ == "__main__":
    units = float(input("Enter units consumed: "))
    bill = calculate_bill(units)
    for key, value in bill.items():
        print(f"{key.replace('_', ' ').title()}: {value:.2f}")
