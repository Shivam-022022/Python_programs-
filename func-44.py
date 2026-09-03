# Take a list of numbers, use filter() and lambda to find numbers greater
# than 50.

numbers = [12, 55, 43, 78, 90, 22, 66]
greater_than_50 = list(filter(lambda x: x > 50, numbers))

if __name__ == "__main__":
    print(f"Numbers: {numbers}")
    print(f"Numbers greater than 50: {greater_than_50}")
