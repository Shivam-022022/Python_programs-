products = [
    ("Laptop", 50000, 1),
    ("Mouse", 500, 2),
    ("Keyboard", 1500, 2),
    ("Headphone", 2000, 1)
]


# a) Calculate total value
total_values = list(
    map(lambda product:
        (product[0], product[1], product[2], product[1] * product[2]),
        products)
)

print("Products with total value:")
print(total_values)


# b) Products costing more than 1000
expensive = list(
    filter(lambda product: product[1] > 1000, products)
)

print("Products costing more than 1000:")
print(expensive)


# c) Sort according to total value
sorted_products = sorted(
    total_values,
    key=lambda product: product[3]
)

print("Products sorted by total value:")
print(sorted_products)