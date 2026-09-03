# Take a list of tuples containing student names and marks, sort the students
# according to their marks using lambda.

students = [("Ritesh", 85), ("Aditi", 92), ("Sahil", 76), ("Meena", 88)]
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)

if __name__ == "__main__":
    print(f"Students: {students}")
    print(f"Sorted by marks (desc): {sorted_students}")
