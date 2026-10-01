import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Aarav", "Diya", "Rohan", "Sneha", "Karan"],
    "Department": ["CSE", "IT", "CSE", "ECE", "IT"],
    "Total_Classes": [100, 100, 100, 100, 100],
    "Classes_Attended": [92, 70, 85, 60, 74],
}
df = pd.DataFrame(data)

df["Attendance Percentage"] = (df["Classes_Attended"] / df["Total_Classes"]) * 100
print("DataFrame:\n", df)

print("\nStudents whose attendance is below 75%:\n",
      df[df["Attendance Percentage"] < 75])
