import os
import pandas as pd

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "patients.csv")
df = pd.read_csv(path)

print("Patients above 60 years:\n", df[df["Age"] > 60])
print("\nAverage medical expense:", df["Medical_Expense"].mean())
print("\nPatient with the highest medical expense:\n",
      df.loc[df["Medical_Expense"].idxmax()])
print("\nNumber of patients for each disease:\n", df["Disease"].value_counts())
print("\nPatients whose medical expense exceeds Rs.50,000:\n",
      df[df["Medical_Expense"] > 50000])
