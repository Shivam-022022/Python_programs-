# Define a function that accepts a string and returns the number of vowels present in it.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)


if __name__ == "__main__":
    text = input("Enter a string: ")
    print(f"Number of vowels = {count_vowels(text)}")
