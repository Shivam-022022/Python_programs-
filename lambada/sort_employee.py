employees = [
    ("Siddhant", 40000),
    ("Rahul", 60000),
    ("Amit", 50000),
    ("Rohit", 70000)
]

result = sorted(employees, key=lambda employee: employee[1])

print("Employees sorted by salary:")
print(result)