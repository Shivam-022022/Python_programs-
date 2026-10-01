class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary

    def display(self):
        print(f"{self.emp_id} | {self.name} | Total Salary: {self.calculate_salary()}")


class Manager(Employee):
    def calculate_salary(self):
        # HRA 30% + Travel allowance 10% + Special allowance 5000
        return self.basic_salary * 1.40 + 5000


class Developer(Employee):
    def calculate_salary(self):
        # HRA 20% + Internet/Tech allowance 3000
        return self.basic_salary * 1.20 + 3000


class Tester(Employee):
    def calculate_salary(self):
        # HRA 15% + Testing allowance 2000
        return self.basic_salary * 1.15 + 2000


for emp in (Manager(1, "Amit", 60000), Developer(2, "Priya", 50000), Tester(3, "Rahul", 40000)):
    emp.display()
