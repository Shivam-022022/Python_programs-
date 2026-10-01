import pandas as pd

data = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005],
    "Customer": ["Amit", "Priya", "Rahul", "Neha", "Suresh"],
    "Product": ["Laptop", "Mouse", "Monitor", "Keyboard", "Printer"],
    "Quantity": [1, 4, 2, 3, 1],
    "Price": [45000, 600, 8500, 1200, 7000],
    "Discount": [2000, 100, 500, 200, 300],
}
df = pd.DataFrame(data)

df["Final Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All orders:\n", df)
print("\nOrders above Rs.5,000:\n", df[df["Final Amount"] > 5000])
print("\nHighest-value order:\n", df.loc[df["Final Amount"].idxmax()])
print("\nAverage order value:", df["Final Amount"].mean())
