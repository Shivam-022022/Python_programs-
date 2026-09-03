# Accept 10 numbers from the user and store them in a list. Calculate:
# • Sum
# • Average

numbers = []

for i in range(10):
    numbers.append(int(input("Enter number: ")))

total = 0
for number in numbers:
    total += number

average = total / 10
print("Sum:", total)
print("Average:", average)
