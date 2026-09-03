# Create a dictionary containing student names and marks. Find the
# student with the lowest marks.

def lowest_scorer(marks_dict):
    return min(marks_dict, key=marks_dict.get)


if __name__ == "__main__":
    marks = {"Ritesh": 85, "Aditi": 92, "Sahil": 76, "Meena": 88}
    print(f"Marks: {marks}")
    bottom_student = lowest_scorer(marks)
    print(f"Lowest scorer: {bottom_student} with {marks[bottom_student]} marks")
