class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def start(self):
        print("Car: Insert key / press button, engine starts smoothly.")


class Bike(Vehicle):
    def start(self):
        print("Bike: Kick-start or press self-start, engine roars.")


class Bus(Vehicle):
    def start(self):
        print("Bus: Driver turns the ignition, air brakes release.")


for v in (Car(), Bike(), Bus()):
    v.start()
