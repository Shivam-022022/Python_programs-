# Create two dictionaries and merge them into a single dictionary.

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


if __name__ == "__main__":
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    print(f"Dict1: {dict1}")
    print(f"Dict2: {dict2}")
    print(f"Merged: {merge_dictionaries(dict1, dict2)}")
