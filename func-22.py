# Write a function that accepts a list of numbers and returns the minimum, maximum,
# sum, and average.

def list_stats(numbers):
    return {
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
    }


if __name__ == "__main__":
    nums = [23, 65, 12, 89, 34]
    stats = list_stats(nums)
    print(f"List: {nums}")
    for key, value in stats.items():
        print(f"{key.capitalize()} = {value}")
