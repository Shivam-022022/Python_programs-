# Create sets representing products belonging to different categories.
# Find products that belong to both categories.

def common_products(category1, category2):
    return category1 & category2


if __name__ == "__main__":
    electronics = {"Laptop", "Mouse", "Headphones", "Smartwatch"}
    accessories = {"Mouse", "Smartwatch", "Bag", "Charger"}

    print(f"Electronics category: {electronics}")
    print(f"Accessories category: {accessories}")
    print(f"Products in both categories: {common_products(electronics, accessories)}")
