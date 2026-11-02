list1 = [10, 20, 30, 40]
list2 = [1, 2, 3, 4]

result = list(map(lambda a, b: a + b, list1, list2))

print("Sum =", result)