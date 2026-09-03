# Create a dictionary containing student marks. Update the marks of a
# specified student.

def update_marks(marks_dict, student, new_marks):
    marks_dict[student] = new_marks
    return marks_dict


if __name__ == "__main__":
    marks = {"Ritesh": 85, "Aditi": 92, "Sahil": 76}
    print(f"Original: {marks}")

    updated = update_marks(marks, "Sahil", 80)
    print(f"Updated: {updated}")
