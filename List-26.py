# Store marks of 20 students in a list and determine:
# • Highest marks
# • Lowest marks
# • Average marks
# • Number of students scoring above average
# • Number of students scoring below average

marks = []

for i in range(20):
    marks.append(float(input("Enter marks: ")))

highest = marks[0]
lowest = marks[0]
total = 0

for mark in marks:
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark
    total += mark

average = total / len(marks)
above = 0
below = 0

for mark in marks:
    if mark > average:
        above += 1
    elif mark < average:
        below += 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Above average:", above)
print("Below average:", below)
