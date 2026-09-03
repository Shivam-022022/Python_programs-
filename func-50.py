# Take employee records containing name, department, and salary, use filter(),
# map(), and sorted() with lambda functions to:
# - Find employees earning more than Rs. 50,000.
# - Increase salaries by 10%.
# - Sort employees according to salary.

employees = [
    ("Amit", "Sales", 45000),
    ("Priya", "IT", 62000),
    ("Rohan", "HR", 38000),
    ("Sneha", "IT", 71000),
]


def employees_above_50k(emp_list):
    return list(filter(lambda e: e[2] > 50000, emp_list))


def increase_salary(emp_list, percent=10):
    return list(map(lambda e: (e[0], e[1], e[2] * (1 + percent / 100)), emp_list))


def sort_by_salary(emp_list):
    return sorted(emp_list, key=lambda e: e[2], reverse=True)


if __name__ == "__main__":
    print(f"Employees: {employees}")

    above_50k = employees_above_50k(employees)
    print(f"Employees earning more than Rs.50,000: {above_50k}")

    increased = increase_salary(employees)
    print(f"After 10% salary increase: {increased}")

    sorted_emps = sort_by_salary(increased)
    print(f"Sorted by salary (desc): {sorted_emps}")
