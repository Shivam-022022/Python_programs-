# Two students have selected different subjects. Store their subjects in
# two sets and determine the subjects studied by both students.

def common_subjects(subjects1, subjects2):
    return subjects1 & subjects2


if __name__ == "__main__":
    student1_subjects = {"Maths", "Physics", "Chemistry", "Computer Science"}
    student2_subjects = {"Biology", "Physics", "Computer Science", "English"}

    print(f"Student 1: {student1_subjects}")
    print(f"Student 2: {student2_subjects}")
    print(f"Common subjects: {common_subjects(student1_subjects, student2_subjects)}")
