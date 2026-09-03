# Create two sets and determine whether the first set is a subset of the
# second set.

def is_subset(set1, set2):
    return set1.issubset(set2)


if __name__ == "__main__":
    set1 = {2, 3}
    set2 = {1, 2, 3, 4, 5}
    print(f"Set1: {set1}")
    print(f"Set2: {set2}")
    print(f"Is Set1 a subset of Set2: {is_subset(set1, set2)}")
