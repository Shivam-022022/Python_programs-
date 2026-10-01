import math


class Shape:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Shape:", self.name)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


for shape in (Circle(5), Rectangle(4, 6), Triangle(3, 8)):
    shape.display_name()
    print("Area:", round(shape.area(), 2))
    print("-" * 20)
