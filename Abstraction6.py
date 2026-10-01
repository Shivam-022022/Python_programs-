from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2           # Rs.2 per km


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 1.5         # Rs.1.5 per km


class Taxi(Transport):
    def calculate_fare(self, distance):
        return 50 + distance * 12     # base fare + Rs.12 per km


class Flight(Transport):
    def calculate_fare(self, distance):
        return 2000 + distance * 6    # base fare + Rs.6 per km


distance = 300
for t in (Bus(), Train(), Taxi(), Flight()):
    print(f"{type(t).__name__:<7} fare for {distance} km: Rs.{t.calculate_fare(distance)}")
