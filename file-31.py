# Create a package student containing:
#   a) marks.py       -- total and percentage
#   b) grade.py       -- grade calculation
#   c) attendance.py  -- attendance eligibility
# Write a main program that uses all three modules to generate a student
# report.
#
# NOTE: A real package would be a "student/" directory with __init__.py,
# marks.py, grade.py, and attendance.py as separate files. It is
# simulated here in one file using clearly labelled sections so it
# matches the file-XX.py naming convention.

# ---------- student/marks.py ----------
def total_marks(marks_list):
    return sum(marks_list)


def percentage(total, num_subjects):
    return total / num_subjects
# ---------- end student/marks.py ----------


# ---------- student/grade.py ----------
def calculate_grade(pct):
    if pct >= 90:
        return "A+"
    elif pct >= 75:
        return "A"
    elif pct >= 60:
        return "B"
    elif pct >= 40:
        return "C"
    else:
        return "Fail"
# ---------- end student/grade.py ----------


# ---------- student/attendance.py ----------
def is_eligible(attendance_percent, minimum_required=75):
    return attendance_percent >= minimum_required
# ---------- end student/attendance.py ----------


def generate_student_report(name, marks_list, attendance_percent):
    total = total_marks(marks_list)
    pct = percentage(total, len(marks_list))
    grade = calculate_grade(pct)
    eligible = is_eligible(attendance_percent)

    return {
        "name": name,
        "total": total,
        "percentage": pct,
        "grade": grade,
        "attendance": attendance_percent,
        "exam_eligible": eligible,
    }


if __name__ == "__main__":
    report = generate_student_report("Ritesh Agale", [85, 90, 78, 92, 88], 80)
    for key, value in report.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
