# Store employee ID, name, department, and salary in a file. Write
# functions to:
# - Display all employees.
# - Find the highest-paid employee.
# - Calculate average salary.
# - Display employees earning above a given salary.

def create_employee_file(filename):
    employees = [
        "E01,Amit,Sales,45000",
        "E02,Priya,IT,62000",
        "E03,Rohan,HR,38000",
        "E04,Sneha,IT,71000",
    ]
    with open(filename, "w") as f:
        f.write("\n".join(employees) + "\n")


def read_employees(filename):
    employees = []
    with open(filename, "r") as f:
        for line in f:
            emp_id, name, dept, salary = line.strip().split(",")
            employees.append({"id": emp_id, "name": name, "department": dept, "salary": int(salary)})
    return employees


def display_all_employees(employees):
    for e in employees:
        print(e)


def highest_paid_employee(employees):
    return max(employees, key=lambda e: e["salary"])


def average_salary(employees):
    return sum(e["salary"] for e in employees) / len(employees)


def employees_above_salary(employees, threshold):
    return [e for e in employees if e["salary"] > threshold]


if __name__ == "__main__":
    create_employee_file("employees.csv")
    employees = read_employees("employees.csv")

    display_all_employees(employees)
    print(f"\nHighest Paid: {highest_paid_employee(employees)}")
    print(f"Average Salary: {average_salary(employees):.2f}")
    print(f"Employees earning above 50000: {employees_above_salary(employees, 50000)}")
