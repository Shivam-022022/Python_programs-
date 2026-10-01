class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def info(self):
        print(f"Brand: {self.brand}, Wheels: {self.wheels}")


class Car(Vehicle):                 # hierarchical
    def __init__(self, brand, seats):
        super().__init__(brand, 4)
        self.seats = seats

    def info(self):
        super().info()
        print("Seats:", self.seats)


class Bike(Vehicle):                # hierarchical
    def __init__(self, brand, engine_cc):
        super().__init__(brand, 2)
        self.engine_cc = engine_cc

    def info(self):
        super().info()
        print("Engine (cc):", self.engine_cc)


class SportsCar(Car):               # multilevel: Vehicle -> Car -> SportsCar
    def __init__(self, brand, seats, top_speed):
        super().__init__(brand, seats)
        self.top_speed = top_speed

    def info(self):
        super().info()
        print("Top Speed (km/h):", self.top_speed)


class ElectricBike(Bike):           # multilevel: Vehicle -> Bike -> ElectricBike
    def __init__(self, brand, battery_kwh):
        super().__init__(brand, 0)
        self.battery_kwh = battery_kwh

    def info(self):
        super().info()
        print("Battery (kWh):", self.battery_kwh)


print("--- Sports Car ---")
SportsCar("Ferrari", 2, 340).info()
print("--- Electric Bike ---")
ElectricBike("Ather", 3.7).info()
