# Write a function check_even_odd(n) that determines whether a given number is even or odd.

def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is {check_even_odd(num)}")
