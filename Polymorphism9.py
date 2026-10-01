class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = (self.feet + other.feet) * 12 + (self.inches + other.inches)
        return Distance(total_inches // 12, total_inches % 12)   # normalized form

    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"


d1 = Distance(5, 8)
d2 = Distance(3, 9)
print("Distance 1:", d1)
print("Distance 2:", d2)
print("Sum       :", d1 + d2)
