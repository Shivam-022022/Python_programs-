class ElectricityBill:

    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 3
        elif self.units <= 200:
            bill = 100*3 + (self.units-100)*5
        else:
            bill = 100*3 + 100*5 + (self.units-200)*8
        return bill


consumer_no = input("Enter consumer number: ")
consumer_name = input("Enter consumer name: ")
units = int(input("Enter units consumed: "))

bill_obj = ElectricityBill(consumer_no, consumer_name, units)

print("Electricity Bill =", bill_obj.calculate_bill())