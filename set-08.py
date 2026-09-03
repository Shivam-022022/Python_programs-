# Create a list containing duplicate numbers, use a set to remove the
# duplicates.

def remove_duplicates(numbers_list):
    return list(set(numbers_list))


if __name__ == "__main__":
    numbers_list = [5, 3, 8, 3, 5, 9, 8, 1]
    print(f"Original list: {numbers_list}")
    print(f"After removing duplicates: {remove_duplicates(numbers_list)}")
