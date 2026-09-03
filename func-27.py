# Create functions to calculate consultation charges, laboratory charges,
# medicine charges, room charges, and final bill. Apply discounts based on
# patient category.

def consultation_charges(visits, rate=300):
    return visits * rate


def lab_charges(tests, rate=250):
    return tests * rate


def medicine_charges(amount):
    return amount


def room_charges(days, rate_per_day=1000):
    return days * rate_per_day


def apply_category_discount(total, category):
    discounts = {"General": 0, "Senior Citizen": 0.15, "Staff": 0.25}
    discount_rate = discounts.get(category, 0)
    return total * discount_rate


def final_bill(visits, tests, medicine_amt, days, category="General"):
    subtotal = (
        consultation_charges(visits)
        + lab_charges(tests)
        + medicine_charges(medicine_amt)
        + room_charges(days)
    )
    discount = apply_category_discount(subtotal, category)
    return subtotal - discount


if __name__ == "__main__":
    total = final_bill(visits=3, tests=2, medicine_amt=800, days=2, category="Senior Citizen")
    print(f"Final Hospital Bill = Rs. {total:.2f}")
