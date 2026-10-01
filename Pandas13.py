import os
import pandas as pd

# Read students.csv (kept in the same folder as this script)
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.csv")
df = pd.read_csv(path)

print("First 5 records:\n", df.head())
print("\nLast 5 records:\n", df.tail())

subjects = ["Python", "DBMS", "Maths"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)
print("\nTotal and average marks of each student:\n", df[["Name", "Total", "Average"]])

print("\nStudents whose average marks are greater than 75:\n", df[df["Average"] > 75])
print("\nStudent with the highest average:\n", df.loc[df["Average"].idxmax()])
print("\nAverage marks for each subject:\n", df[subjects].mean())
