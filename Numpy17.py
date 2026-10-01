import numpy as np

marks = np.array([78, 85, 92, 67, 74, 88, 95, 58, 81, 70,
                  62, 99, 45, 73, 84, 90, 55, 68, 77, 86])
print("Marks of 20 students:", marks)

average = np.mean(marks)
print("Class average:", average)
print("Students who scored above average:", marks[marks > average])
