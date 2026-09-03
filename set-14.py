# Create two sets and determine whether the first set is a superset of
# the second set.

def is_superset(set1, set2):
    return set1.issuperset(set2)


if __name__ == "__main__":
    set1 = {1, 2, 3, 4, 5}
    set2 = {2, 3}
    print(f"Set1: {set1}")
    print(f"Set2: {set2}")
    print(f"Is Set1 a superset of Set2: {is_superset(set1, set2)}")
