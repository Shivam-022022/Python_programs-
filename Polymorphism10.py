class Student:
    def __init__(self, name, total_marks):
        self.name = name
        self.total_marks = total_marks

    def __gt__(self, other):
        return self.total_marks > other.total_marks

    def __lt__(self, other):
        return self.total_marks < other.total_marks


s1 = Student("Aarav", 450)
s2 = Student("Diya", 480)

print(f"{s1.name}: {s1.total_marks}, {s2.name}: {s2.total_marks}")
print(f"{s1.name} > {s2.name} :", s1 > s2)
print(f"{s1.name} < {s2.name} :", s1 < s2)
if s1 > s2:
    print(s1.name, "scored higher.")
elif s1 < s2:
    print(s2.name, "scored higher.")
else:
    print("Both scored equally.")
