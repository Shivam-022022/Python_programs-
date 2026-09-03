# Given two dictionaries, identify the values that are common to both
# dictionaries.

def common_values(dict1, dict2):
    return set(dict1.values()) & set(dict2.values())


if __name__ == "__main__":
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"x": 2, "y": 3, "z": 4}
    print(f"Dict1: {dict1}")
    print(f"Dict2: {dict2}")
    print(f"Common values: {common_values(dict1, dict2)}")
