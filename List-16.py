# Create a nested list storing:
# • Student Name
# • Roll Number
# • Marks
# Display all student details.

students = [
    ["Rohan", 1, 85],
    ["Amit", 2, 78],
    ["Sneha", 3, 92],
    ["Priya", 4, 88]
]

for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
