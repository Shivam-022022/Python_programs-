# Accept two lists and merge them into a single list.

list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

merged = list1 + list2
print("Merged list:", merged)
