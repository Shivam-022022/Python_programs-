students = [
    ("Siddhant", 85),
    ("Rahul", 70),
    ("Amit", 95),
    ("Rohit", 60)
]

result = sorted(students, key=lambda student: student[1])

print("Students sorted by marks:")
print(result)