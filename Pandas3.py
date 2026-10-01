import pandas as pd

data = {
    "Product ID": [1, 2, 3, 4, 5],
    "Product Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Computers", "Accessories", "Accessories", "Displays", "Office"],
    "Price": [55000, 500, 1200, 9000, 7500],
    "Quantity": [3, 40, 25, 10, 6],
}
df = pd.DataFrame(data)

df["Total Amount"] = df["Price"] * df["Quantity"]
print("DataFrame:\n", df)

best = df.loc[df["Total Amount"].idxmax()]
print("\nProduct with the highest total sales:")
print(best["Product Name"], "-", best["Total Amount"])
