# Create a function to find the second-largest number in a list.

def second_largest(numbers):
    unique_sorted = sorted(set(numbers), reverse=True)
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]


if __name__ == "__main__":
    nums = [12, 45, 3, 89, 34, 89]
    print(f"List: {nums}")
    print(f"Second largest = {second_largest(nums)}")
