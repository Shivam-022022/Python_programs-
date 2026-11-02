import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 15, 25]
y2 = [5, 15, 20, 30]

plt.plot(x, y1, label="Class A")
plt.plot(x, y2, label="Class B")
plt.title("Class Performance")
plt.xlabel("Test")
plt.ylabel("Marks")
plt.legend()
plt.show()
