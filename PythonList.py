#1. Create a list of five fruits and display the list
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("Fruits:", fruits)

#2. Display first, last, and third element
numbers = [10, 20, 30, 40, 50]

print("First:", numbers[0])
print("Last:", numbers[-1])
print("Third:", numbers[2])


#3. Replace third color
colors = ["Red", "Blue", "Green", "Yellow"]

colors[2] = "Purple"

print(colors)

#4. Add elements to a list
numbers = [10, 20, 30]

numbers.append(40)
numbers.insert(0, 5)
numbers.insert(2, 15)

print(numbers)


#5. Remove students
students = ["Amit", "Rahul", "Priya", "Sneha", "Kiran"]

students.pop(0)
students.pop()

students.remove("Priya")

print(students)


#6. Largest and smallest without max() and min()
numbers = [12, 45, 3, 89, 23]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)


#7. Accept 10 numbers and find sum & average
numbers = []

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)


#8. Count even and odd numbers
numbers = [2,5,8,11,14,17,20,23,26,29,30,33,36,39,40]

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)


#9. Search city
cities = ["Pune", "Mumbai", "Delhi", "Chennai"]

city = input("Enter city: ")

if city in cities:
    print("City Found")
else:
    print("City Not Found")


#10. Reverse without reverse()
numbers = [10,20,30,40,50]

rev = []

for i in range(len(numbers)-1, -1, -1):
    rev.append(numbers[i])

print(rev)


#11. List slicing
numbers = [1,2,3,4,5,6,7,8,9,10]

print("First 5:", numbers[:5])
print("Last 5:", numbers[-5:])
print("Middle 4:", numbers[3:7])
print("Alternate:", numbers[::2])
print("Reverse:", numbers[::-1])


#12. Elements at even index
numbers = [10,20,30,40,50,60,70]

print("Even Index Elements:")

for i in range(0, len(numbers), 2):
    print(numbers[i])


#13. Sort ascending and descending
numbers = []

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

numbers.sort()
print("Ascending:", numbers)

numbers.sort(reverse=True)
print("Descending:", numbers)


#14. Display unique elements
numbers = [1,2,2,3,4,4,5,6,6]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print(unique)


#15. Second largest element
numbers = [12,45,67,89,34]

numbers.sort()

print("Second Largest:", numbers[-2])


#16. Nested list for students
students = [
    ["Amit",101,85],
    ["Rahul",102,90],
    ["Priya",103,95]
]

for student in students:
    print("Name:", student[0])
    print("Roll:", student[1])
    print("Marks:", student[2])
    print()


#17. Matrix addition
A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

B = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

C = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Result:")
for row in C:
    print(row)


#18. Shopping cart
cart = ["Milk","Bread","Eggs"]

cart.append("Butter")
cart.remove("Bread")

item = input("Search item: ")

if item in cart:
    print("Item Found")
else:
    print("Not Found")

print(cart)
print("Total Items:", len(cart))


#19. Student attendance
students = ["Amit","Rahul","Priya"]

print("Total Students:", len(students))

name = input("Search Student: ")

if name in students:
    print("Present")
else:
    print("Absent")

students.append("Sneha")
students.remove("Rahul")

print(students)


#20. Book list
books = ["Python","Java","C++"]

books.append("AI")

book = input("Search Book: ")

if book in books:
    print("Book Found")
else:
    print("Book Not Found")

books.remove("Java")

print(books)
print("Total Books:", len(books))


#21. Merge two lists
list1 = [1,2,3]
list2 = [4,5,6]

merged = list1 + list2

print(merged)


#22. Common elements
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

common = []

for i in list1:
    if i in list2:
        common.append(i)

print(common)


#23. Frequency of each element
numbers = [1,2,2,3,3,3,4]

for i in numbers:
    print(i, ":", numbers.count(i))


#24. Rotate list
numbers = [1,2,3,4,5]

left = numbers[1:] + numbers[:1]
right = numbers[-1:] + numbers[:-1]

print("Left Rotation:", left)
print("Right Rotation:", right)


#25. Remove duplicates while preserving order
numbers = [1,2,2,3,4,3,5]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print(unique)


#26. Student marks analysis
marks = [45,67,78,89,90,56,44,77,80,91,66,73,88,59,61,92,54,68,71,83]

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above = 0
below = 0

for i in marks:
    if i > average:
        above += 1
    elif i < average:
        below += 1

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Above Average:", above)
print("Below Average:", below)


#27. Employee salaries
salary = [25000,45000,60000,52000,28000]

print("Highest:", max(salary))
print("Lowest:", min(salary))
print("Average:", sum(salary)/len(salary))

above = 0
below = 0

for s in salary:
    if s > 50000:
        above += 1
    if s < 30000:
        below += 1

print("Above 50000:", above)
print("Below 30000:", below)


#28. Batsman scores
scores = [45,60,120,80,30,110,55,90,100,40]

print("Highest:", max(scores))
print("Lowest:", min(scores))
print("Total:", sum(scores))
print("Average:", sum(scores)/len(scores))

century = 0
half = 0

for s in scores:
    if s >= 100:
        century += 1
    elif s >= 50:
        half += 1

print("Centuries:", century)
print("Half Centuries:", half)


#29. Temperature analysis
temp = [30,32,35,31,33,36,37,38,34,32,
        31,33,35,36,37,39,40,34,33,32,
        31,30,29,35,36,38,37,34,33,32]

highest = max(temp)
lowest = min(temp)
avg = sum(temp)/len(temp)

above = 0
below = 0

for t in temp:
    if t > avg:
        above += 1
    elif t < avg:
        below += 1

print("Hottest:", highest)
print("Coldest:", lowest)
print("Average:", avg)
print("Above Average:", above)
print("Below Average:", below)


#30. Patient management
patients = ["Rahul", "Amit", "Priya"]
ages = [30, 45, 28]

patients.append("Sneha")
ages.append(35)

name = input("Search Patient: ")

if name in patients:
    index = patients.index(name)
    print("Found:", patients[index], "Age:", ages[index])
else:
    print("Patient Not Found")

patients.remove("Amit")
ages.pop(1)

print("\nPatient List")

for i in range(len(patients)):
    print(patients[i], "-", ages[i])

print("Total Patients:", len(patients))