# Create a directory named ecommerce containing packages for:
#   a) Products
#   b) Customers
#   c) Orders
#   d) Payments
# Each package should contain at least two modules.
#
# NOTE: A real project would use "products/", "customers/", "orders/",
# and "payments/" packages, each with at least two modules. It is
# simulated here in one file using clearly labelled sections so it
# matches the file-XX.py naming convention used for this exercise set.

# ---------- products package ----------
# products/catalog.py
products = {}


def add_product(product_id, name, price):
    products[product_id] = {"name": name, "price": price}


# products/inventory.py
inventory = {}


def update_stock(product_id, quantity):
    inventory[product_id] = inventory.get(product_id, 0) + quantity
# ---------- end products package ----------


# ---------- customers package ----------
# customers/profile.py
customers = {}


def add_customer(customer_id, name, email):
    customers[customer_id] = {"name": name, "email": email}


# customers/address.py
addresses = {}


def add_address(customer_id, address):
    addresses[customer_id] = address
# ---------- end customers package ----------


# ---------- orders package ----------
# orders/cart.py
def calculate_order_total(product_ids):
    return sum(products[pid]["price"] for pid in product_ids)


# orders/status.py
order_status = {}


def set_order_status(order_id, status):
    order_status[order_id] = status
# ---------- end orders package ----------


# ---------- payments package ----------
# payments/processor.py
def process_payment(amount, method="Card"):
    return f"Payment of Rs.{amount} processed via {method}"


# payments/invoice.py
def generate_invoice(order_id, amount):
    return f"Invoice for Order {order_id}: Rs.{amount}"
# ---------- end payments package ----------


if __name__ == "__main__":
    add_product("P01", "Laptop", 55000)
    add_product("P02", "Mouse", 500)
    update_stock("P01", 10)

    add_customer("C01", "Ritesh Agale", "ritesh@example.com")
    add_address("C01", "Kolhapur, Maharashtra")

    total = calculate_order_total(["P01", "P02"])
    set_order_status("O01", "Confirmed")

    print(process_payment(total))
    print(generate_invoice("O01", total))
    print(f"Order Status: {order_status['O01']}")
