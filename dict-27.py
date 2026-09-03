# Create a dictionary containing product names and quantities.
#
# Perform:
# - Add a product
# - Update quantity
# - Delete a product
# - Search for a product
# - Display products with quantity below 10

products = {"Laptop": 15, "Mouse": 5, "Keyboard": 8, "Monitor": 20}


def add_product(name, quantity):
    products[name] = quantity


def update_quantity(name, quantity):
    if name in products:
        products[name] = quantity
        return True
    return False


def delete_product(name):
    return products.pop(name, None) is not None


def search_product(name):
    return products.get(name, "Product not found")


def low_stock_products(threshold=10):
    return {name: qty for name, qty in products.items() if qty < threshold}


if __name__ == "__main__":
    add_product("Webcam", 3)
    update_quantity("Mouse", 12)

    print(f"All products: {products}")
    print(f"Search 'Keyboard': {search_product('Keyboard')}")
    print(f"Low stock (<10): {low_stock_products()}")

    delete_product("Monitor")
    print(f"After deleting Monitor: {products}")
