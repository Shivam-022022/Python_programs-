# Create the following directory structure:
#   college_project/
#     main.py
#     student/
#       __init__.py
#       details.py
#       marks.py
#     faculty/
#       __init__.py
#       details.py
# Write a program that imports functions from both packages and displays
# student and faculty information.
#
# NOTE: A real project would be split across the directory structure
# shown above. It is simulated here in one file using clearly labelled
# sections representing each module, so it matches the file-XX.py
# naming convention used for this exercise set.

# ---------- student/details.py ----------
def get_student_details(name, roll_no, branch):
    return {"name": name, "roll_no": roll_no, "branch": branch}
# ---------- end student/details.py ----------


# ---------- student/marks.py ----------
def get_student_marks(marks_list):
    total = sum(marks_list)
    percentage = total / len(marks_list)
    return {"total": total, "percentage": percentage}
# ---------- end student/marks.py ----------


# ---------- faculty/details.py ----------
def get_faculty_details(name, department, designation):
    return {"name": name, "department": department, "designation": designation}
# ---------- end faculty/details.py ----------


if __name__ == "__main__":
    student = get_student_details("Ritesh Agale", 21, "Computer Science")
    marks = get_student_marks([85, 90, 78, 92, 88])
    faculty = get_faculty_details("Dr. Sharma", "Computer Science", "Professor")

    print("Student Information:")
    print(student)
    print(marks)

    print("\nFaculty Information:")
    print(faculty)
