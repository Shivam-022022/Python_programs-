import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 12, 18, 20]

plt.plot(x, y)
plt.axvline(x=3, linestyle="--", label="Reference Line")
plt.title("Vertical Line")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.show()
