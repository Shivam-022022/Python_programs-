# Write a program to append additional student information to an existing
# file without deleting its previous contents.

def append_student_info(filename, info):
    with open(filename, "a") as f:
        f.write(info + "\n")


if __name__ == "__main__":
    with open("student.txt", "w") as f:
        f.write("Name: Ritesh Agale\nRoll No: 21\n")

    append_student_info("student.txt", "Branch: Computer Science")
    append_student_info("student.txt", "Semester: 5")

    with open("student.txt") as f:
        print(f.read())
