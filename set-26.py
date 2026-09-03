# Find students enrolled in both courses and students enrolled in only
# one course (extension of the Python/Java enrollment problem, using a
# third course to demonstrate the general case across multiple sets).

def enrolled_in_all(*course_sets):
    result = course_sets[0]
    for s in course_sets[1:]:
        result = result & s
    return result


def enrolled_in_exactly_one(*course_sets):
    all_students = set()
    for s in course_sets:
        all_students |= s

    exactly_one = set()
    for student in all_students:
        count = sum(1 for s in course_sets if student in s)
        if count == 1:
            exactly_one.add(student)
    return exactly_one


if __name__ == "__main__":
    python_students = {"Ritesh", "Aditi", "Sahil"}
    java_students = {"Sahil", "Meena", "Karan"}
    web_dev_students = {"Meena", "Priya", "Ritesh"}

    print(f"Python: {python_students}")
    print(f"Java: {java_students}")
    print(f"Web Dev: {web_dev_students}")
    print(f"Enrolled in all three: {enrolled_in_all(python_students, java_students, web_dev_students)}")
    print(f"Enrolled in exactly one course: {enrolled_in_exactly_one(python_students, java_students, web_dev_students)}")
