# Check whether a string is a palindrome using recursion.

def is_palindrome_recursive(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])


if __name__ == "__main__":
    text = input("Enter a string: ")
    result = is_palindrome_recursive(text)
    print(f"'{text}' is {'a Palindrome' if result else 'not a Palindrome'}")
