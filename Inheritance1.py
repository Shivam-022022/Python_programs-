class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary          # monthly salary

    def display(self):
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Salary      :", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department  :", self.department)

    def annual_salary(self):
        return self.salary * 12


emp = Employee(101, "Amit", 40000)
mgr = Manager(201, "Priya", 80000, "Sales")

print("--- Employee Details ---")
emp.display()
print("--- Manager Details ---")
mgr.display()
print("Manager's annual salary:", mgr.annual_salary())
