class StudentResult:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return (self.calculate_total() / 500) * 100

    def calculate_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 60:
            return "C"
        else:
            return "D"

    def __del__(self):
        print("Result processing for", self.name, "completed")


name = input("Enter student name: ")
marks = []

for i in range(5):
    m = int(input("Enter marks for subject " + str(i+1) + ": "))
    marks.append(m)

student = StudentResult(name, marks)

print("Total =", student.calculate_total())
print("Percentage =", student.calculate_percentage())
print("Grade =", student.calculate_grade())

del student