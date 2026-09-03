# Create a dictionary containing student names and marks. Find the
# student who has scored the highest marks.

def highest_scorer(marks_dict):
    return max(marks_dict, key=marks_dict.get)


if __name__ == "__main__":
    marks = {"Ritesh": 85, "Aditi": 92, "Sahil": 76, "Meena": 88}
    print(f"Marks: {marks}")
    top_student = highest_scorer(marks)
    print(f"Highest scorer: {top_student} with {marks[top_student]} marks")
