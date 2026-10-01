import os
import pandas as pd

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "employees.csv")
df = pd.read_csv(path)

print("Employees from the CSE department:\n", df[df["Department"] == "CSE"])
print("\nAverage salary:", df["Salary"].mean())
print("Highest salary:", df["Salary"].max())
print("Lowest salary:", df["Salary"].min())
print("\nEmployees with salary greater than Rs.50,000:\n", df[df["Salary"] > 50000])
print("\nDepartment-wise average salary:\n", df.groupby("Department")["Salary"].mean())
