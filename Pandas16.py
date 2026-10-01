import os
import pandas as pd

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "weather.csv")
df = pd.read_csv(path)

print("Maximum temperature:", df["Temperature"].max())
print("Minimum temperature:", df["Temperature"].min())
print("Average temperature:", df["Temperature"].mean())
print("\nRecords where temperature is above 35 C:\n", df[df["Temperature"] > 35])
print("\nCity-wise average temperature:\n", df.groupby("City")["Temperature"].mean())
