# Take employee records containing name and salary, sort them according to
# salary using lambda.

employees = [("Amit", 45000), ("Priya", 62000), ("Rohan", 38000), ("Sneha", 71000)]
sorted_employees = sorted(employees, key=lambda e: e[1], reverse=True)

if __name__ == "__main__":
    print(f"Employees: {employees}")
    print(f"Sorted by salary (desc): {sorted_employees}")
