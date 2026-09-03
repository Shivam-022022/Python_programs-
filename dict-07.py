# Create a dictionary containing student records and find the total
# number of key-value pairs.

def total_pairs(dictionary):
    return len(dictionary)


if __name__ == "__main__":
    student = {"roll_no": 21, "name": "Ritesh Agale", "department": "Computer Science", "marks": 88}
    print(f"Student record: {student}")
    print(f"Total key-value pairs = {total_pairs(student)}")
