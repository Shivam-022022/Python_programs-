class Person:
    def display_role(self):
        print("I am a person.")


class Student(Person):
    def display_role(self):
        print("Role: Student - I attend classes and write exams.")


class Faculty(Person):
    def display_role(self):
        print("Role: Faculty - I teach and guide students.")


class Administrator(Person):
    def display_role(self):
        print("Role: Administrator - I manage college operations.")


people = [Student(), Faculty(), Administrator()]
for person in people:
    person.display_role()
