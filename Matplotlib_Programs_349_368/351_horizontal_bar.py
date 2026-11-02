import matplotlib.pyplot as plt

languages = ["Python", "Java", "C", "JavaScript"]
students = [40, 30, 20, 25]

plt.barh(languages, students)
plt.title("Programming Language Preferences")
plt.xlabel("Number of Students")
plt.ylabel("Languages")
plt.show()
