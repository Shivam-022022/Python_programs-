# Create two sets of numbers and find the elements that are present in
# either set but not in both.

def symmetric_difference(set1, set2):
    return set1 ^ set2


if __name__ == "__main__":
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(f"Set1: {set1}")
    print(f"Set2: {set2}")
    print(f"Symmetric Difference: {symmetric_difference(set1, set2)}")
