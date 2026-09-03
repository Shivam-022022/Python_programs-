# Create a set of student names. Ask the user to enter a name and check
# whether the student exists in the set.

def check_student_exists(student_set, name):
    return name in student_set


if __name__ == "__main__":
    students = {"Ritesh", "Aditi", "Sahil", "Meena"}
    print(f"Students: {students}")

    name = input("Enter a name to check: ")
    exists = check_student_exists(students, name)
    print(f"{name} {'exists' if exists else 'does not exist'} in the set")
