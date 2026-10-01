class Animal:
    def sound(self):
        print("Some animal sound")


class Dog(Animal):
    def sound(self):
        print("Dog: Woof! Woof!")


class Cat(Animal):
    def sound(self):
        print("Cat: Meow!")


class Cow(Animal):
    def sound(self):
        print("Cow: Moo!")


class Lion(Animal):
    def sound(self):
        print("Lion: Roar!")


for a in (Dog(), Cat(), Cow(), Lion()):
    a.sound()
