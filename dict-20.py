# Create a dictionary and display its elements in ascending order of
# keys.

def sort_by_keys(dictionary):
    return dict(sorted(dictionary.items()))


if __name__ == "__main__":
    data = {"banana": 3, "apple": 5, "cherry": 2, "date": 8}
    print(f"Original: {data}")
    print(f"Sorted by keys: {sort_by_keys(data)}")
