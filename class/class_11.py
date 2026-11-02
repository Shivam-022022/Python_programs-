class ShoppingCart:

    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []
        print("Shopping cart created for", self.customer_name)

    def add_product(self, name, price):
        self.products.append({"name": name, "price": price})

    def remove_product(self, name):
        self.products = [p for p in self.products if p["name"] != name]

    def calculate_total(self):
        total = 0
        for product in self.products:
            total = total + product["price"]
        return total

    def __del__(self):
        print("Shopping cart of", self.customer_name, "destroyed")


customer_name = input("Enter customer name: ")
cart_id = input("Enter cart ID: ")

cart = ShoppingCart(customer_name, cart_id)

n = int(input("How many products to add? "))
for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    cart.add_product(name, price)

print("Total Bill =", cart.calculate_total())

del cart