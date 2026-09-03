# Take a dictionary containing student names and their departments;
# create a new dictionary that groups students according to their
# department.

def group_by_department(student_dept):
    grouped = {}
    for student, dept in student_dept.items():
        grouped.setdefault(dept, []).append(student)
    return grouped


if __name__ == "__main__":
    student_dept = {
        "Ritesh": "Computer Science",
        "Aditi": "Electronics",
        "Sahil": "Computer Science",
        "Meena": "Mechanical",
        "Karan": "Electronics",
    }
    print(f"Student-Department: {student_dept}")
    print(f"Grouped by department: {group_by_department(student_dept)}")
