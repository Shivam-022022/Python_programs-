# Create a dictionary and display:
# - All keys
# - All values
# - All key-value pairs

def display_dict_info(dictionary):
    return {
        "keys": list(dictionary.keys()),
        "values": list(dictionary.values()),
        "items": list(dictionary.items()),
    }


if __name__ == "__main__":
    student = {"roll_no": 21, "name": "Ritesh Agale", "marks": 88}
    info = display_dict_info(student)

    print(f"Keys: {info['keys']}")
    print(f"Values: {info['values']}")
    print(f"Key-Value Pairs: {info['items']}")
