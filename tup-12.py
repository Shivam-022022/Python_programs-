# Problem Statement:
# Accept five numbers from the user, store them in a list, and convert the list into a tuple.

# Answer:
numbers = []
for i in range(5):
    numbers.append(int(input("Enter number: ")))
values = tuple(numbers)
print(values)
