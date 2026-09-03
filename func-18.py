# Create a function that accepts marks in five subjects and returns the student's
# percentage and grade.

def percentage_and_grade(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"

    return percentage, grade


if __name__ == "__main__":
    marks = [85, 90, 78, 92, 88]
    percentage, grade = percentage_and_grade(*marks)
    print(f"Marks: {marks}")
    print(f"Percentage = {percentage:.2f}%, Grade = {grade}")
