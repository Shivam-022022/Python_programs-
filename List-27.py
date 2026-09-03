# Store salaries of employees and determine:
# • Highest salary
# • Lowest salary
# • Average salary
# • Employees earning above ₹50,000
# • Employees earning below ₹30,000

salaries = list(map(float, input("Enter employee salaries: ").split()))

highest = salaries[0]
lowest = salaries[0]
total = 0
above_50000 = 0
below_30000 = 0

for salary in salaries:
    if salary > highest:
        highest = salary
    if salary < lowest:
        lowest = salary
    total += salary

    if salary > 50000:
        above_50000 += 1
    if salary < 30000:
        below_30000 += 1

average = total / len(salaries)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("Employees above ₹50,000:", above_50000)
print("Employees below ₹30,000:", below_30000)
