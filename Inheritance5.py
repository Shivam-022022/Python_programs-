class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name           :", self.name)
        print("Age            :", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def display(self):
        super().display()
        print("Roll No        :", self.roll_no)
        print("Course         :", self.course)


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        super().display()
        print("Research Topic :", self.topic)
        print("Guide Name     :", self.guide)


ResearchStudent("Kavya", 25, 501, "Ph.D. CSE", "Machine Learning", "Dr. Sharma").display()
