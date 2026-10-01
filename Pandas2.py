import pandas as pd

data = {
    "Employee ID": [1, 2, 3, 4, 5],
    "Employee Name": ["Amit", "Priya", "Rahul", "Neha", "Suresh"],
    "Department": ["CSE", "HR", "CSE", "Finance", "IT"],
    "Salary": [62000, 38000, 85000, 47000, 55000],
    "Experience": [5, 3, 8, 4, 6],
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

print("\nEmployees with salary greater than Rs.50,000:\n", df[df["Salary"] > 50000])
print("\nAverage salary:", df["Salary"].mean())
print("Highest salary:", df["Salary"].max())
print("\nEmployee with the highest experience:\n", df.loc[df["Experience"].idxmax()])
