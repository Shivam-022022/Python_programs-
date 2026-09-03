# Create a function that checks whether a given string or number is a palindrome.

def is_palindrome(value):
    s = str(value)
    return s == s[::-1]


if __name__ == "__main__":
    val = input("Enter a string or number: ")
    print(f"{val} is {'a Palindrome' if is_palindrome(val) else 'not a Palindrome'}")
