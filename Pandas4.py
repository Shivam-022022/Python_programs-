import pandas as pd

data = {
    "Patient ID": ["P01", "P02", "P03", "P04", "P05"],
    "Patient Name": ["Ramesh", "Sunita", "Gopal", "Lata", "Arjun"],
    "Age": [67, 54, 72, 61, 35],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Diabetes", "Fever"],
    "Medical Charges": [45000, 8000, 120000, 52000, 6000],
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

print("\nPatients above 60 years:\n", df[df["Age"] > 60])
print("\nAverage medical charge:", df["Medical Charges"].mean())
print("Maximum medical charge:", df["Medical Charges"].max())
print("\nPatients with medical charges greater than Rs.50,000:\n",
      df[df["Medical Charges"] > 50000])
