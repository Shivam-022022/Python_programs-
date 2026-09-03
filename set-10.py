# Create two sets and find the elements common to both sets.

def find_intersection(set1, set2):
    return set1 & set2


if __name__ == "__main__":
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(f"Set1: {set1}")
    print(f"Set2: {set2}")
    print(f"Common elements: {find_intersection(set1, set2)}")
