employees = [
    ("Siddhant", "IT", 60000),
    ("Rahul", "HR", 45000),
    ("Amit", "IT", 70000),
    ("Rohit", "Sales", 50000)
]


# a) Employees earning more than 50000
high_salary = list(
    filter(lambda employee: employee[2] > 50000, employees)
)

print("Employees earning more than 50000:")
print(high_salary)


# b) Increase salary by 10%
new_salaries = list(
    map(lambda employee:
        (employee[0], employee[1], employee[2] * 1.10),
        employees)
)

print("After 10% salary increase:")
print(new_salaries)


# c) Sort according to salary
sorted_employees = sorted(
    new_salaries,
    key=lambda employee: employee[2]
)

print("Sorted employees:")
print(sorted_employees)