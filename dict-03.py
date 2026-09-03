# Create a dictionary of five products and their prices. Add a new
# product and price to the dictionary.

def add_product(products, name, price):
    products[name] = price
    return products


if __name__ == "__main__":
    products = {"Laptop": 55000, "Mouse": 500, "Keyboard": 800, "Monitor": 9000, "Headphones": 1500}
    print(f"Original: {products}")

    updated = add_product(products, "Webcam", 2000)
    print(f"Updated: {updated}")
