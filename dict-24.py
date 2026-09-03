# Create a dictionary containing integers from 1 to 10 and their cubes.

def numbers_and_cubes(n=10):
    return {i: i ** 3 for i in range(1, n + 1)}


if __name__ == "__main__":
    result = numbers_and_cubes(10)
    print(f"Numbers and their cubes: {result}")
