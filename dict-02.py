# Create a dictionary containing employee information and display the
# value associated with a specified key.

def get_value(dictionary, key):
    return dictionary.get(key, "Key not found")


if __name__ == "__main__":
    employee = {"id": "E01", "name": "Priya Sharma", "department": "IT", "salary": 62000}
    print(f"Employee: {employee}")
    print(f"Value for 'name': {get_value(employee, 'name')}")
