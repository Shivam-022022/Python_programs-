# Write a program using separate functions to process student records containing
# name, roll number, and marks in five subjects. Calculate total, percentage,
# grade, class average, highest scorer, and lowest scorer.

def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total, num_subjects=5):
    return total / num_subjects


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"


def process_students(students):
    processed = []
    for student in students:
        total = calculate_total(student["marks"])
        percentage = calculate_percentage(total)
        grade = calculate_grade(percentage)
        processed.append({
            "name": student["name"],
            "roll_no": student["roll_no"],
            "total": total,
            "percentage": percentage,
            "grade": grade,
        })
    return processed


def class_average(processed):
    return sum(s["percentage"] for s in processed) / len(processed)


def highest_scorer(processed):
    return max(processed, key=lambda s: s["percentage"])


def lowest_scorer(processed):
    return min(processed, key=lambda s: s["percentage"])


if __name__ == "__main__":
    students = [
        {"name": "Ritesh", "roll_no": 1, "marks": [85, 90, 78, 92, 88]},
        {"name": "Aditi", "roll_no": 2, "marks": [70, 65, 80, 75, 60]},
        {"name": "Sahil", "roll_no": 3, "marks": [55, 60, 50, 45, 65]},
    ]

    processed = process_students(students)
    for s in processed:
        print(f"{s['name']} (Roll {s['roll_no']}): Total={s['total']}, "
              f"Percentage={s['percentage']:.2f}%, Grade={s['grade']}")

    print(f"\nClass Average = {class_average(processed):.2f}%")
    print(f"Highest Scorer = {highest_scorer(processed)['name']}")
    print(f"Lowest Scorer = {lowest_scorer(processed)['name']}")
