# Create a list of student names. Remove:
# • First student
# • Last student
# • A specific student by name
# Display the remaining list.

students = ["Rohan", "Amit", "Sneha", "Priya", "Rahul"]
students.pop(0)
students.pop()
students.remove("Sneha")
print(students)
