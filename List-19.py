# Store names of students present in class.
# Display:
# • Total students
# • Search a student's attendance
# • Add a new student
# • Remove an absent student

students = ["Rohan", "Amit", "Sneha", "Priya"]

print("Total students:", len(students))

name = input("Enter student name to search: ")
if name in students:
    print("Student is present")
else:
    print("Student is absent")

new_student = input("Enter new student: ")
students.append(new_student)

absent_student = input("Enter absent student to remove: ")
if absent_student in students:
    students.remove(absent_student)

print("Students:", students)
