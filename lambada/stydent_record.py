students = [
    ("Siddhant", 85),
    ("Rahul", 70),
    ("Amit", 90),
    ("Rohit", 60),
    ("Akash", 80)
]


def calculate_average(students):
    total = 0

    for student in students:
        total = total + student[1]

    return total / len(students)


# a) Average
average = calculate_average(students)

print("Average marks =", average)


# b) Students scoring above 75
above_75 = list(filter(lambda student: student[1] > 75, students))

print("Students above 75 =", above_75)


# c) Sort according to marks
sorted_students = sorted(students, key=lambda student: student[1])

print("Sorted students =", sorted_students)