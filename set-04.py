# Create a set of numbers and remove a specified number from the set.

def remove_number(number_set, number):
    number_set.discard(number)
    return number_set


if __name__ == "__main__":
    numbers = {10, 20, 30, 40, 50}
    print(f"Original set: {numbers}")

    updated = remove_number(numbers, 30)
    print(f"After removing 30: {updated}")
