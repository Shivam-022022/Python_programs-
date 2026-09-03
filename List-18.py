# Create a shopping cart using a list.
# Perform:
# • Add item
# • Remove item
# • Search item
# • Display cart
# • Count total items

cart = ["Milk", "Bread", "Apples"]

cart.append(input("Enter item to add: "))

item = input("Enter item to remove: ")
if item in cart:
    cart.remove(item)

search = input("Enter item to search: ")
if search in cart:
    print("Item found")
else:
    print("Item not found")

print("Cart:", cart)
print("Total items:", len(cart))
