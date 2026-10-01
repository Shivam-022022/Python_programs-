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
        print("Roll Number    :", self.roll_no)
        print("Course         :", self.course)


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        super().display()
        print("Research Topic :", self.research_topic)
        print("Guide Name     :", self.guide_name)


rs = ResearchStudent("Ishaan", 26, 702, "M.Tech", "Data Mining", "Dr. Verma")
rs.display()
