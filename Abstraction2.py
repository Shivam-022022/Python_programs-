from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car engine started.")

    def stop(self):
        print("Car engine stopped.")


class Bike(Vehicle):
    def start(self):
        print("Bike started with a kick.")

    def stop(self):
        print("Bike stopped using brakes.")


class Bus(Vehicle):
    def start(self):
        print("Bus engine started.")

    def stop(self):
        print("Bus stopped at the bus stop.")


for v in (Car(), Bike(), Bus()):
    v.start()
    v.stop()
    print("-" * 25)
