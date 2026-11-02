class MobilePhone:

    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specs(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def price_after_discount(self, discount_percent):
        return self.price - (self.price * discount_percent / 100)


brand = input("Enter brand: ")
model = input("Enter model: ")
storage = input("Enter storage: ")
price = float(input("Enter price: "))

phone = MobilePhone(brand, model, storage, price)
phone.display_specs()

discount_percent = float(input("Enter discount percent: "))
print("Price after discount =", phone.price_after_discount(discount_percent))