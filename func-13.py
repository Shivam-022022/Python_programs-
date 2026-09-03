# Write a function that accepts a list of numbers and returns their average.

def average(numbers):
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50]
    print(f"List: {nums}")
    print(f"Average = {average(nums)}")
