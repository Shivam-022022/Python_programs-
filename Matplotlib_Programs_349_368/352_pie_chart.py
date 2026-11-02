import matplotlib.pyplot as plt

labels = ["Python", "Java", "C", "C++"]
values = [35, 30, 20, 15]

plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.title("Programming Language Distribution")
plt.show()
