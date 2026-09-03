# Create sets representing students enrolled in:
# - Python
# - Java
#
# Find students enrolled in both courses and students enrolled in only
# one course.

def enrolled_in_both(python_students, java_students):
    return python_students & java_students


def enrolled_in_only_one(python_students, java_students):
    return python_students ^ java_students


if __name__ == "__main__":
    python_students = {"Ritesh", "Aditi", "Sahil"}
    java_students = {"Sahil", "Meena", "Karan"}

    print(f"Python students: {python_students}")
    print(f"Java students: {java_students}")
    print(f"Enrolled in both: {enrolled_in_both(python_students, java_students)}")
    print(f"Enrolled in only one: {enrolled_in_only_one(python_students, java_students)}")
