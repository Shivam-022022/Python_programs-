# Take a list of integers, use filter() and lambda to extract all even numbers.

numbers = [10, 15, 22, 33, 44, 51, 60]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

if __name__ == "__main__":
    print(f"Numbers: {numbers}")
    print(f"Even Numbers: {even_numbers}")
