# Create a dictionary containing student names and marks. Develop a
# program to:
# - Add a student
# - Update marks
# - Delete a student
# - Search for a student
# - Display all students
# - Find the highest marks
# - Calculate the average

students = {"Ritesh": 85, "Aditi": 92, "Sahil": 76}


def add_student(name, marks):
    students[name] = marks


def update_marks(name, marks):
    if name in students:
        students[name] = marks
        return True
    return False


def delete_student(name):
    return students.pop(name, None) is not None


def search_student(name):
    return students.get(name, "Student not found")


def display_all_students():
    return students


def highest_marks_student():
    return max(students, key=students.get)


def average_marks():
    return sum(students.values()) / len(students)


if __name__ == "__main__":
    add_student("Meena", 88)
    update_marks("Sahil", 80)

    print(f"All students: {display_all_students()}")
    print(f"Search 'Aditi': {search_student('Aditi')}")
    print(f"Highest scorer: {highest_marks_student()}")
    print(f"Average marks: {average_marks():.2f}")

    delete_student("Sahil")
    print(f"After deleting Sahil: {display_all_students()}")
