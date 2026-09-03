# Create a module student.py containing functions to calculate total
# marks, percentage, and grade. Import the module into another Python
# program and generate a student's result.
#
# NOTE: Combined into a single file. The "student module" section below
# represents what would normally live in student.py.

# ---------- student module ----------
def total_marks(marks_list):
    return sum(marks_list)


def percentage(total, num_subjects):
    return total / num_subjects


def grade(pct):
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
# ---------- end student module ----------


def generate_result(name, marks_list):
    total = total_marks(marks_list)
    pct = percentage(total, len(marks_list))
    g = grade(pct)
    return {"name": name, "total": total, "percentage": pct, "grade": g}


if __name__ == "__main__":
    result = generate_result("Ritesh Agale", [85, 90, 78, 92, 88])
    print(result)
