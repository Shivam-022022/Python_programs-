# Accept 10 numbers and sort them in:
# • Ascending order
# • Descending order

numbers = []

for i in range(10):
    numbers.append(int(input("Enter number: ")))

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Ascending:", ascending)
print("Descending:", descending)
