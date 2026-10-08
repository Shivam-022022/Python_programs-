import csv
employees = [
    ["ID", "Name", "Department", "Salary"],
    [101, "Alice", "HR", 45000],
    [102, "Bob", "IT", 65000],
    [103, "Charlie", "Finance", 55000],
    [104, "David", "IT", 75000],
    [105, "Eva", "HR", 40000]
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(employees)

salary_limit = float(input("Enter salary: "))

print("\nEmployees with salary above", salary_limit, ":")

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for employee in reader:
        if float(employee["Salary"]) > salary_limit:
            print(
                employee["ID"],
                employee["Name"],
                employee["Department"],
                employee["Salary"]
            )