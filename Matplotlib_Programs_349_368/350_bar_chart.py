import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C", "DBMS"]
marks = [85, 78, 90, 82]

plt.bar(subjects, marks)
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
