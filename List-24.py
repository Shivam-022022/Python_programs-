# Rotate a list:
# • Left by one position
# • Right by one position

numbers = list(map(int, input("Enter list elements: ").split()))

if numbers:
    left = numbers[1:] + numbers[:1]
    right = numbers[-1:] + numbers[:-1]
    print("Left rotation:", left)
    print("Right rotation:", right)
else:
    print("List is empty")
