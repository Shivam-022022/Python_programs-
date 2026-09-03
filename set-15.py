# Write a program to determine whether two sets have no elements in
# common.

def are_disjoint(set1, set2):
    return set1.isdisjoint(set2)


if __name__ == "__main__":
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    print(f"Set1: {set1}")
    print(f"Set2: {set2}")
    print(f"Are disjoint: {are_disjoint(set1, set2)}")
