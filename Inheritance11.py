class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, m1, m2, m3):
        super().__init__(roll_no, name, course)
        self.marks = [m1, m2, m3]

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def grade(self):
        p = self.percentage()
        if p >= 90:
            return "A+"
        elif p >= 80:
            return "A"
        elif p >= 70:
            return "B"
        elif p >= 60:
            return "C"
        elif p >= 40:
            return "D"
        return "F"

    def display(self):
        print("Roll No    :", self.roll_no)
        print("Name       :", self.name)
        print("Course     :", self.course)
        print("Marks      :", self.marks)
        print("Total      :", self.total())
        print("Percentage :", round(self.percentage(), 2))
        print("Grade      :", self.grade())


Result(1, "Aarav", "B.Tech", 88, 92, 79).display()
