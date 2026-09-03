# Create a set of five fruits. Add two new fruits using appropriate set
# methods and display the updated set.

def add_fruits(fruit_set, new_fruits):
    fruit_set.update(new_fruits)
    return fruit_set


if __name__ == "__main__":
    fruits = {"apple", "banana", "mango", "grape", "orange"}
    print(f"Original set: {fruits}")

    updated = add_fruits(fruits, ["kiwi", "papaya"])
    print(f"Updated set: {updated}")
