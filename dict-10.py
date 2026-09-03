# Accept five student names and their marks from the user and store them
# in a dictionary.

def collect_student_marks(num_students=5):
    students = {}
    for i in range(num_students):
        name = input(f"Enter name of student {i + 1}: ")
        marks = float(input(f"Enter marks of {name}: "))
        students[name] = marks
    return students


if __name__ == "__main__":
    students = collect_student_marks(5)
    print(f"Student Marks: {students}")
