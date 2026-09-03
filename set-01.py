# Write a Python program to create a set containing five integers and
# display all its elements.

def create_and_display_set():
    numbers = {10, 20, 30, 40, 50}
    return numbers


if __name__ == "__main__":
    numbers = create_and_display_set()
    print(f"Set of integers: {numbers}")
    for num in numbers:
        print(num)
