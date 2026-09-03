# Create a list containing duplicate values. Convert the list into a set
# and display the resulting set.

def list_to_set(lst):
    return set(lst)


if __name__ == "__main__":
    numbers_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
    print(f"List: {numbers_list}")
    print(f"Set (duplicates removed): {list_to_set(numbers_list)}")
