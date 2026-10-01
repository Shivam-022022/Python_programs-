class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_personal(self):
        print("Name        :", self.name)
        print("Age         :", self.age)


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary

    def show_professional(self):
        print("Employee ID :", self.emp_id)
        print("Designation :", self.designation)
        print("Salary      :", self.salary)


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print("--- Complete Employee Information ---")
        self.show_personal()
        self.show_professional()


Employee("Neha", 29, "E101", "Software Engineer", 75000).display()
