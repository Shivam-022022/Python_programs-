# Store student attendance records in a file. Calculate the attendance
# percentage and display students having attendance below 75%.

def create_attendance_file(filename):
    records = ["Amit,60,80", "Priya,75,80", "Rohan,50,80", "Sneha,78,80"]
    # format: name, classes_attended, total_classes
    with open(filename, "w") as f:
        f.write("\n".join(records) + "\n")


def read_attendance(filename):
    records = []
    with open(filename, "r") as f:
        for line in f:
            name, attended, total = line.strip().split(",")
            records.append({"name": name, "attended": int(attended), "total": int(total)})
    return records


def calculate_percentage(record):
    return (record["attended"] / record["total"]) * 100


def students_below_75(records):
    return [r for r in records if calculate_percentage(r) < 75]


if __name__ == "__main__":
    create_attendance_file("attendance.csv")
    records = read_attendance("attendance.csv")

    for r in records:
        print(f"{r['name']}: {calculate_percentage(r):.2f}%")

    print("\nStudents below 75% attendance:")
    for r in students_below_75(records):
        print(f"{r['name']}: {calculate_percentage(r):.2f}%")
