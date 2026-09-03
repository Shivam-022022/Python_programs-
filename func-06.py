# Define a function to calculate the area of a circle using its radius.

import math

def area_of_circle(radius):
    return math.pi * radius ** 2


if __name__ == "__main__":
    r = float(input("Enter radius: "))
    print(f"Area of circle = {area_of_circle(r):.2f}")
