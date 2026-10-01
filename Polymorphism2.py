class Employee:
    def __init__(self, name, basic):
        self.name = name
        self.basic = basic

    def calculate_salary(self):
        return self.basic


class Manager(Employee):
    def calculate_salary(self):
        return self.basic + 0.40 * self.basic + 8000    # HRA/TA + bonus


class Developer(Employee):
    def calculate_salary(self):
        return self.basic + 0.25 * self.basic + 4000    # HRA + tech allowance


class Tester(Employee):
    def calculate_salary(self):
        return self.basic + 0.15 * self.basic + 2000    # HRA + testing allowance


for e in [Manager("Amit", 70000), Developer("Priya", 55000), Tester("Rahul", 40000)]:
    print(f"{e.name} ({type(e).__name__}) salary: {e.calculate_salary()}")
