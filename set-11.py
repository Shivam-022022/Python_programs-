# Create two sets and find:
# - Elements present in the first set but not the second
# - Elements present in the second set but not the first

def difference_first_not_second(set1, set2):
    return set1 - set2


def difference_second_not_first(set1, set2):
    return set2 - set1


if __name__ == "__main__":
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(f"Set1: {set1}")
    print(f"Set2: {set2}")
    print(f"In Set1 but not Set2: {difference_first_not_second(set1, set2)}")
    print(f"In Set2 but not Set1: {difference_second_not_first(set1, set2)}")
