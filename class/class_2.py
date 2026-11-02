class Employee:

    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def calculate_gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()


emp_id = input("Enter employee ID: ")
name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))

emp = Employee(emp_id, name, basic_salary)

print("HRA =", emp.calculate_hra())
print("DA =", emp.calculate_da())
print("Gross Salary =", emp.calculate_gross_salary())