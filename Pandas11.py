import pandas as pd

ages = {"P01": 67, "P02": 54, "P03": 72, "P04": 61, "P05": 35}
s = pd.Series(ages)

print("Series:\n", s)
print("\nAverage age:", s.mean())
print("Oldest patient:", s.idxmax(), "- Age", s.max())
print("Youngest patient:", s.idxmin(), "- Age", s.min())
print("\nPatients above 60 years:\n", s[s > 60])
