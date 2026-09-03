# Create a file containing student records in the format:
# RollNo,Name,Marks
# 101,Amit,85
# 102,Priya,92
# 103,Rahul,78
#
# Write a program to:
# - Display all records.
# - Find the student with the highest marks.
# - Calculate average marks.
# - Display students who scored more than 80.

def create_records_file(filename):
    records = ["101,Amit,85", "102,Priya,92", "103,Rahul,78"]
    with open(filename, "w") as f:
        f.write("\n".join(records) + "\n")


def read_records(filename):
    records = []
    with open(filename, "r") as f:
        for line in f:
            roll_no, name, marks = line.strip().split(",")
            records.append({"roll_no": roll_no, "name": name, "marks": int(marks)})
    return records


def display_all_records(records):
    for r in records:
        print(f"Roll No: {r['roll_no']}, Name: {r['name']}, Marks: {r['marks']}")


def highest_scorer(records):
    return max(records, key=lambda r: r["marks"])


def average_marks(records):
    return sum(r["marks"] for r in records) / len(records)


def students_above_80(records):
    return [r for r in records if r["marks"] > 80]


if __name__ == "__main__":
    create_records_file("students.csv")
    records = read_records("students.csv")

    display_all_records(records)
    print(f"\nHighest Scorer: {highest_scorer(records)}")
    print(f"Average Marks: {average_marks(records):.2f}")
    print(f"Students scoring above 80: {students_above_80(records)}")
