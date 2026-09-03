# Create a dictionary containing student details such as roll number,
# name, department, and marks. Display all key-value pairs.

def create_student_dict():
    return {"roll_no": 21, "name": "Ritesh Agale", "department": "Computer Science", "marks": 88}


if __name__ == "__main__":
    student = create_student_dict()
    for key, value in student.items():
        print(f"{key}: {value}")
