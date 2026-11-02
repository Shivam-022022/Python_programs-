import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker="o")
plt.title("Graph with Grid")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.show()
