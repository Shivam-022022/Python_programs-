# Find common elements between two lists.

list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("Common elements:", common)
