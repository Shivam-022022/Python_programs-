class Academic:
    def __init__(self, marks):
        self.marks = marks            # out of 100

    def show_marks(self):
        print("Academic marks:", self.marks)


class Sports:
    def __init__(self, points):
        self.points = points          # out of 100

    def show_points(self):
        print("Sports points :", self.points)


class Student(Academic, Sports):
    def __init__(self, name, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)
        self.name = name

    def overall_performance(self):
        # 70% weightage to academics, 30% to sports
        return self.marks * 0.7 + self.points * 0.3


s = Student("Rohan", 85, 90)
print("Student:", s.name)
s.show_marks()
s.show_points()
print("Overall performance:", s.overall_performance())
