class Person:
    def __init__(self, name, age, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age

    def display(self):
        print("Name :", self.name)
        print("Age  :", self.age)


class Student(Person):                      # hierarchical: Person -> Student
    def __init__(self, roll_no, **kwargs):
        super().__init__(**kwargs)
        self.roll_no = roll_no

    def display(self):
        super().display()
        print("Roll No :", self.roll_no)


class Faculty(Person):                      # hierarchical: Person -> Faculty
    def __init__(self, employee_id, subject, **kwargs):
        super().__init__(**kwargs)
        self.employee_id = employee_id
        self.subject = subject

    def display(self):
        super().display()
        print("Employee ID :", self.employee_id)
        print("Subject     :", self.subject)


class TeachingAssistant(Student, Faculty):  # multiple inheritance
    def __init__(self, stipend, **kwargs):
        super().__init__(**kwargs)
        self.stipend = stipend

    def display(self):
        super().display()
        print("Stipend :", self.stipend)


ta = TeachingAssistant(
    name="Sneha", age=24, roll_no=301,
    employee_id="TA01", subject="Python", stipend=15000
)
print("--- Teaching Assistant Details ---")
ta.display()
print()
print("Method Resolution Order:", [c.__name__ for c in TeachingAssistant.__mro__])
