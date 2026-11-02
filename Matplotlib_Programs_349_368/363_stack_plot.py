import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
study = [2, 3, 2, 4, 3]
sports = [1, 2, 3, 1, 2]
other = [2, 1, 2, 2, 1]

plt.stackplot(days, study, sports, other, labels=["Study", "Sports", "Other"])
plt.title("Daily Time Distribution")
plt.xlabel("Day")
plt.ylabel("Hours")
plt.legend(loc="upper left")
plt.show()
