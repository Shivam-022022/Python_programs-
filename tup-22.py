# Problem Statement:
# Roll Number
# Name
# Department
# Marks
# Display all the details.

# Answer:
employees = (
    (101, "Ritesh", 50000),
    (102, "Amit", 60000),
    (103, "Sneha", 55000)
)

for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print()
