import math


class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Runtime polymorphism: the same call resolves to different methods
shapes = [Circle(7), Rectangle(5, 10), Triangle(6, 4)]
for s in shapes:
    print(f"{type(s).__name__} area = {round(s.area(), 2)}")
