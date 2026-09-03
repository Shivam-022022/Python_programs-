# Use map() with lambda to calculate the cube of every element in a list.

numbers = [1, 2, 3, 4, 5]
cubes = list(map(lambda x: x ** 3, numbers))

if __name__ == "__main__":
    print(f"Numbers: {numbers}")
    print(f"Cubes: {cubes}")
