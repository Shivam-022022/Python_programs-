import pandas as pd

attendance = {"Aarav": 92.5, "Diya": 70.0, "Rohan": 85.0, "Sneha": 60.5, "Karan": 94.0}
s = pd.Series(attendance)

print("Series:\n", s)
print("\nAverage attendance:", s.mean())
print("\nStudents with attendance below 75%:\n", s[s < 75])
print("\nStudents with attendance above 90%:\n", s[s > 90])
print("\nHighest attendance:", s.max(), "(", s.idxmax(), ")")
