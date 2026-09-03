# Take a list containing student names and marks, use functions and lambda
# expressions to:
# - Calculate average marks.
# - Filter students scoring above 75.
# - Sort students according to marks.

students = [("Ritesh", 85), ("Aditi", 92), ("Sahil", 68), ("Meena", 76), ("Karan", 55)]


def average_marks(students_list):
    return sum(map(lambda s: s[1], students_list)) / len(students_list)


def students_above_75(students_list):
    return list(filter(lambda s: s[1] > 75, students_list))


def sort_students_by_marks(students_list):
    return sorted(students_list, key=lambda s: s[1], reverse=True)


if __name__ == "__main__":
    print(f"Students: {students}")
    print(f"Average Marks: {average_marks(students):.2f}")
    print(f"Students scoring above 75: {students_above_75(students)}")
    print(f"Sorted by marks (desc): {sort_students_by_marks(students)}")
