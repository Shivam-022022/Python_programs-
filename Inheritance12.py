class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display(self):
        print("Product ID :", self.product_id)
        print("Name       :", self.name)
        print("Price      :", self.price)


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty      # in years

    def display(self):
        super().display()
        print("Brand      :", self.brand)
        print("Warranty   :", self.warranty, "years")

    def final_price(self, discount_percent):
        return self.price - self.price * discount_percent / 100


tv = ElectronicProduct(1, "Smart TV", 45000, "Samsung", 2)
tv.display()
print("Final price after 15% discount:", tv.final_price(15))
