# Take a list of integers and a target value, find two numbers whose sum
# is equal to the target using a dictionary.

def two_sum(numbers, target):
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen[num] = i
    return None


if __name__ == "__main__":
    numbers = [2, 7, 11, 15, 3, 6]
    target = 9
    result = two_sum(numbers, target)
    print(f"Numbers: {numbers}")
    print(f"Target: {target}")
    print(f"Pair with sum {target}: {result}")
