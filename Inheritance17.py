class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sound(self):
        print("Some generic animal sound")


class Dog(Animal):
    def sound(self):
        print(f"{self.name} says: Woof! Woof!")

    def behavior(self):
        print(f"{self.name} wags its tail and guards the house.")


class Cat(Animal):
    def sound(self):
        print(f"{self.name} says: Meow!")

    def behavior(self):
        print(f"{self.name} purrs and chases mice.")


class Cow(Animal):
    def sound(self):
        print(f"{self.name} says: Moo!")

    def behavior(self):
        print(f"{self.name} grazes in the field and gives milk.")


for animal in (Dog("Bruno", 3), Cat("Kitty", 2), Cow("Gauri", 5)):
    animal.eat()
    animal.sound()
    animal.behavior()
    print("-" * 30)
