class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_vehicle(self):
        print("Brand :", self.brand)
        print("Model :", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display_vehicle(self):
        super().display_vehicle()
        print("Fuel  :", self.fuel_type)
        print("Price :", self.price)

    def discounted_price(self, discount_percent):
        return self.price - (self.price * discount_percent / 100)


car = Car("Hyundai", "Creta", "Petrol", 1200000)
car.display_vehicle()
print("Price after 10% discount:", car.discounted_price(10))
