import pandas as pd

sales = {
    "Product_ID": [1, 2, 3, 4, 5, 6],
    "Product_Name": ["Pen", "Notebook", "Bag", "Calculator", "Bottle", "Headphones"],
    "Category": ["Stationery", "Stationery", "Accessories", "Electronics", "Accessories", "Electronics"],
    "Price": [10, 50, 800, 450, 250, 1500],
    "Quantity": [500, 300, 20, 40, 60, 12],
}

# 1. Convert dictionary into DataFrame
df = pd.DataFrame(sales)

# 2 & 3. Add Total_Sales column (Price x Quantity)
df["Total_Sales"] = df["Price"] * df["Quantity"]
print("DataFrame with Total_Sales:\n", df)

# Total of all sales
print("\nTotal sales:", df["Total_Sales"].sum())

# 4. Products with sales greater than Rs.10,000
print("\nProducts with sales greater than Rs.10,000:\n", df[df["Total_Sales"] > 10000])

# 5. Product with maximum sales
print("\nProduct with maximum sales:\n", df.loc[df["Total_Sales"].idxmax()])

# 6. Average sales
print("\nAverage sales:", df["Total_Sales"].mean())
