# Create a dictionary containing student names and marks. Calculate the
# average marks of all students.

def average_marks(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)


if __name__ == "__main__":
    marks = {"Ritesh": 85, "Aditi": 92, "Sahil": 76, "Meena": 88}
    print(f"Marks: {marks}")
    print(f"Average marks = {average_marks(marks):.2f}")
