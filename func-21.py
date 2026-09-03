# Create a function that accepts item prices and quantities and returns the total
# bill after applying a discount.

def total_bill(prices, quantities, discount_percent=0):
    subtotal = sum(p * q for p, q in zip(prices, quantities))
    discount = subtotal * (discount_percent / 100)
    return subtotal - discount


if __name__ == "__main__":
    prices = [100, 250, 60]
    quantities = [2, 1, 5]
    discount = 10
    print(f"Total bill after {discount}% discount = Rs. {total_bill(prices, quantities, discount):.2f}")
