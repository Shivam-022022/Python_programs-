# Create a dictionary containing duplicate values and remove duplicate
# values while retaining the corresponding keys where appropriate.

def remove_duplicate_values(dictionary):
    seen_values = set()
    result = {}
    for key, value in dictionary.items():
        if value not in seen_values:
            result[key] = value
            seen_values.add(value)
    return result


if __name__ == "__main__":
    data = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
    print(f"Original: {data}")
    print(f"After removing duplicate values: {remove_duplicate_values(data)}")
