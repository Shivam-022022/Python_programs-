# Implement functions to add/remove products, calculate subtotal, apply coupon
# discounts, calculate GST, and generate the final invoice.

cart = {}

GST_RATE = 0.18
COUPONS = {"SAVE10": 0.10, "SAVE20": 0.20}


def add_product(name, price, quantity):
    cart[name] = {"price": price, "quantity": quantity}


def remove_product(name):
    if name in cart:
        del cart[name]


def calculate_subtotal():
    return sum(item["price"] * item["quantity"] for item in cart.values())


def apply_coupon(subtotal, coupon_code):
    discount_rate = COUPONS.get(coupon_code, 0)
    return subtotal * discount_rate


def calculate_gst(amount):
    return amount * GST_RATE


def generate_invoice(coupon_code=None):
    subtotal = calculate_subtotal()
    discount = apply_coupon(subtotal, coupon_code) if coupon_code else 0
    taxable_amount = subtotal - discount
    gst = calculate_gst(taxable_amount)
    total = taxable_amount + gst

    return {
        "subtotal": subtotal,
        "discount": discount,
        "gst": gst,
        "total": total,
    }


if __name__ == "__main__":
    add_product("Laptop", 50000, 1)
    add_product("Mouse", 500, 2)

    invoice = generate_invoice(coupon_code="SAVE10")
    for key, value in invoice.items():
        print(f"{key.title()}: Rs. {value:.2f}")
