import pandas as pd

marks = {"Aarav": 85, "Diya": 72, "Rohan": 90, "Sneha": 58, "Karan": 76}
s = pd.Series(marks)

print("Series:\n", s)
print("\nMarks of Rohan:", s["Rohan"])
print("Maximum marks:", s.max())
print("Minimum marks:", s.min())
print("Average marks:", s.mean())
print("\nStudents who scored more than 75:\n", s[s > 75])
