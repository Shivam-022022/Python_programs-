import pandas as pd

prices = {"Laptop": 55000, "Mouse": 500, "Keyboard": 1200, "Monitor": 9000, "Pen": 10}
s = pd.Series(prices)

print("Products and prices:\n", s)

s_new = s * 1.10
print("\nPrices after 10% increase:\n", s_new)

print("\nMost expensive product:", s.idxmax(), "-", s.max())
print("\nProducts costing more than Rs.1,000:\n", s[s > 1000])
