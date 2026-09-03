# Write a lambda function that returns True if a number is even and False
# otherwise.

is_even = lambda x: x % 2 == 0

if __name__ == "__main__":
    num = 7
    print(f"{num} is even: {is_even(num)}")
