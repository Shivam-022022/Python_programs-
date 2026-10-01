import pandas as pd

data = {
    "Student ID": [101, 102, 103, 104, 105],
    "Student Name": ["Aarav", "Diya", "Rohan", "Sneha", "Karan"],
    "Python Marks": [85, 72, 90, 58, 76],
    "DBMS Marks": [78, 65, 88, 62, 80],
    "Mathematics Marks": [92, 70, 95, 55, 74],
}
df = pd.DataFrame(data)

print("DataFrame:\n", df)

subjects = ["Python Marks", "DBMS Marks", "Mathematics Marks"]
df["Total Marks"] = df[subjects].sum(axis=1)
print("\nTotal marks for each student:\n", df[["Student Name", "Total Marks"]])

df["Average Marks"] = df[subjects].mean(axis=1)
print("\nAverage marks:\n", df[["Student Name", "Average Marks"]])

print("\nStudents who scored more than 75% average:\n", df[df["Average Marks"] > 75])
