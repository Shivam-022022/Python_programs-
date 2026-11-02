import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
marks = [35, 45, 55, 65, 75, 90]

plt.scatter(hours, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()
