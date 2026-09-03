# Take two lists of numbers, use map() and lambda to create a third list
# containing the sum of corresponding elements.

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
sum_list = list(map(lambda a, b: a + b, list1, list2))

if __name__ == "__main__":
    print(f"List1: {list1}")
    print(f"List2: {list2}")
    print(f"Sum List: {sum_list}")
