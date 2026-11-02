import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
sales_a = [10, 15, 13, 18, 22]
sales_b = [8, 12, 16, 15, 20]

plt.plot(months, sales_a, label="Product A")
plt.plot(months, sales_b, label="Product B")
plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()
