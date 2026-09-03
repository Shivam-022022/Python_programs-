# Write a Python program to create a file named student.txt and write the
# student's name, roll number, branch, and semester into the file.

def create_student_file(filename, name, roll_no, branch, semester):
    with open(filename, "w") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Roll No: {roll_no}\n")
        f.write(f"Branch: {branch}\n")
        f.write(f"Semester: {semester}\n")


if __name__ == "__main__":
    create_student_file("student.txt", "Ritesh Agale", 21, "Computer Science", 5)
    with open("student.txt") as f:
        print(f.read())
