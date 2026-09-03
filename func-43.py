# Use filter() and lambda to extract positive numbers from a list.

numbers = [-5, 3, -2, 8, -1, 0, 7]
positive_numbers = list(filter(lambda x: x > 0, numbers))

if __name__ == "__main__":
    print(f"Numbers: {numbers}")
    print(f"Positive Numbers: {positive_numbers}")
