# Define a function that accepts a list and an element and returns the number of
# times that element occurs.

def count_occurrences(lst, element):
    return lst.count(element)


if __name__ == "__main__":
    lst = [1, 2, 3, 2, 4, 2, 5]
    elem = 2
    print(f"List: {lst}")
    print(f"{elem} occurs {count_occurrences(lst, elem)} times")
