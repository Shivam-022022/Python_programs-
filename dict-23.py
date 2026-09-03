# Given a list of numbers, create a dictionary containing each unique
# number and its frequency.

def number_frequency(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    return freq


if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
    print(f"Numbers: {numbers}")
    print(f"Frequency: {number_frequency(numbers)}")
