class Student:

    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        percentage = sum(self.marks) / len(self.marks)
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage)


n = int(input("How many students: "))
students = []

for i in range(n):
    roll_no = input("Enter roll number: ")
    name = input("Enter name: ")

    marks = []
    for j in range(3):
        m = int(input("Enter marks for subject " + str(j+1) + ": "))
        marks.append(m)

    student = Student(roll_no, name, marks)
    students.append(student)

for student in students:
    student.display()
    print()