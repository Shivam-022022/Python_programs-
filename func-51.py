# Take a list of products with names, prices, and quantities, use functions and
# lambda expressions to:
# - Calculate total value of each product.
# - Filter products costing more than Rs. 1,000.
# - Sort products according to total value.

products = [
    ("Keyboard", 800, 3),
    ("Monitor", 9000, 2),
    ("Mouse", 500, 5),
    ("Laptop", 55000, 1),
]


def total_value_per_product(product_list):
    return list(map(lambda p: (p[0], p[1] * p[2]), product_list))


def products_above_1000(product_list):
    return list(filter(lambda p: p[1] > 1000, product_list))


def sort_by_total_value(product_list):
    totals = total_value_per_product(product_list)
    return sorted(totals, key=lambda p: p[1], reverse=True)


if __name__ == "__main__":
    print(f"Products: {products}")

    totals = total_value_per_product(products)
    print(f"Total value of each product: {totals}")

    filtered = products_above_1000(products)
    print(f"Products costing more than Rs.1000: {filtered}")

    sorted_totals = sort_by_total_value(products)
    print(f"Sorted by total value (desc): {sorted_totals}")
