import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temperature = [28, 30, 29, 32, 31]

plt.plot(days, temperature, marker="o", linestyle="-")
plt.title("Daily Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.show()
