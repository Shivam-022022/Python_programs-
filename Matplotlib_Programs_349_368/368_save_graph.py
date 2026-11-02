import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

plt.plot(x, y, marker="o")
plt.title("Graph Saved as Image")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.savefig("matplotlib_graph.png")
plt.show()
