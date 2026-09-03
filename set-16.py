# Create two sets and check whether they are equal.

def are_equal(set1, set2):
    return set1 == set2


if __name__ == "__main__":
    set1 = {1, 2, 3}
    set2 = {3, 2, 1}
    print(f"Set1: {set1}")
    print(f"Set2: {set2}")
    print(f"Are equal: {are_equal(set1, set2)}")
