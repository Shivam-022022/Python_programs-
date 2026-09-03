# Write a function that accepts a list of numbers and returns the largest element
# without using the built-in max() function.

def find_largest(numbers):
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest


if __name__ == "__main__":
    nums = [12, 45, 3, 89, 34]
    print(f"List: {nums}")
    print(f"Largest element = {find_largest(nums)}")
