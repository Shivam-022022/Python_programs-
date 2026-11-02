class Vehicle:

    def __init__(self, vehicle_no, model, rental_rate, available):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.available = available

    def rent_vehicle(self, days):
        if self.available:
            self.available = False
            charges = self.rental_rate * days
            print("Vehicle rented for", days, "days. Charges =", charges)
        else:
            print("Vehicle not available")

    def return_vehicle(self):
        self.available = True
        print("Vehicle returned")


vehicle_no = input("Enter vehicle number: ")
model = input("Enter model: ")
rental_rate = float(input("Enter rental rate per day: "))

vehicle = Vehicle(vehicle_no, model, rental_rate, True)

days = int(input("Enter number of rental days: "))
vehicle.rent_vehicle(days)

vehicle.return_vehicle()