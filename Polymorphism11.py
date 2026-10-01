class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Headphones", 2500)
p2 = Product("Speaker", 2500)
p3 = Product("Smartwatch", 4999)

print("Headphones == Speaker    :", p1 == p2)
print("Smartwatch > Headphones  :", p3 > p1)
print("Headphones > Smartwatch  :", p1 > p3)
