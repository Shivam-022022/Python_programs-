# Same problem as Inheritance15, written using __str__ for display.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def __str__(self):
        return super().__str__() + f", Roll No: {self.roll_no}, Course: {self.course}"


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def __str__(self):
        return (super().__str__()
                + f", Research Topic: {self.research_topic}, Guide: {self.guide_name}")


print(Person("Rita", 40))
print(Student("Manav", 21, 101, "B.Sc"))
print(ResearchStudent("Tara", 27, 801, "Ph.D.", "Quantum Computing", "Dr. Rao"))
