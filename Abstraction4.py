from abc import ABC, abstractmethod


class FoodOrder(ABC):
    def __init__(self, items_total):
        self.items_total = items_total

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def calculate_bill(self):
        service_charge = 0.05 * self.items_total
        return self.items_total + service_charge + self.delivery_charge()

    def delivery_charge(self):
        return 0                       # dine-in, no delivery


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, items_total, distance_km):
        super().__init__(items_total)
        self.distance_km = distance_km

    def calculate_bill(self):
        return self.items_total + self.delivery_charge()

    def delivery_charge(self):
        return 20 + 10 * self.distance_km


r = RestaurantOrder(800)
h = HomeDeliveryOrder(800, 5)
print("Restaurant bill   :", r.calculate_bill(), "| Delivery charge:", r.delivery_charge())
print("Home delivery bill:", h.calculate_bill(), "| Delivery charge:", h.delivery_charge())
