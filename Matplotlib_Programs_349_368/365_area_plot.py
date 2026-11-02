import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 12, 20, 25]

plt.fill_between(x, y, alpha=0.5)
plt.plot(x, y)
plt.title("Area Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
