class FoodOrder:

    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def calculate_total_bill(self):
        subtotal = self.quantity * self.price
        tax = subtotal * 0.05
        total = subtotal + tax
        return total

    def __del__(self):
        print("Order", self.order_id, "completed. Thank you", self.customer_name)


order_id = input("Enter order ID: ")
customer_name = input("Enter customer name: ")
food_item = input("Enter food item: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

order = FoodOrder(order_id, customer_name, food_item, quantity, price)

print("Total Bill (with tax) =", order.calculate_total_bill())

del order