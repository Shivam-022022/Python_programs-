import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 10, 8, 15, 20]

plt.plot(x, y, color="red", linestyle="--", linewidth=2, marker="s")
plt.title("Customized Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
