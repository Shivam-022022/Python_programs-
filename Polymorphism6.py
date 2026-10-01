class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        return "Not defined"


class EngineeringStudent(Student):
    def calculate_grade(self):
        if self.marks >= 75:
            return "Distinction"
        elif self.marks >= 60:
            return "First Class"
        elif self.marks >= 40:
            return "Pass"
        return "Fail"


class MedicalStudent(Student):
    def calculate_grade(self):
        if self.marks >= 85:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 50:
            return "C"
        return "Fail"


class ManagementStudent(Student):
    def calculate_grade(self):
        if self.marks >= 80:
            return "A+"
        elif self.marks >= 65:
            return "A"
        elif self.marks >= 50:
            return "B"
        return "Fail"


students = [EngineeringStudent("Aarav", 78), MedicalStudent("Diya", 72),
            ManagementStudent("Rohan", 66)]
for s in students:
    print(f"{s.name} ({type(s).__name__}) - Marks: {s.marks} - Grade: {s.calculate_grade()}")
