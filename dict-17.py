# Given two dictionaries, find the keys that are common to both
# dictionaries.

def common_keys(dict1, dict2):
    return dict1.keys() & dict2.keys()


if __name__ == "__main__":
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"b": 20, "c": 30, "d": 40}
    print(f"Dict1: {dict1}")
    print(f"Dict2: {dict2}")
    print(f"Common keys: {common_keys(dict1, dict2)}")
