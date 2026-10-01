import pandas as pd

salaries = {"Amit": 62000, "Priya": 38000, "Rahul": 85000, "Neha": 47000, "Suresh": 55000}
s = pd.Series(salaries)

print("Series:\n", s)
print("\nHighest salary:", s.max(), "(", s.idxmax(), ")")
print("Lowest salary:", s.min(), "(", s.idxmin(), ")")
print("Average salary:", s.mean())
print("\nEmployees earning more than Rs.50,000:\n", s[s > 50000])
