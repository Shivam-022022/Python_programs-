# Convert a decimal number into binary using recursion without using Python's
# built-in conversion functions.

def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n < 0:
        return "-" + decimal_to_binary(-n)
    if n < 2:
        return str(n)
    return decimal_to_binary(n // 2) + str(n % 2)


if __name__ == "__main__":
    num = int(input("Enter a decimal number: "))
    print(f"Binary of {num} = {decimal_to_binary(num)}")
