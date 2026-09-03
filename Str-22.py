# Run-Length Encoding
# Compress a string by counting consecutive repeated characters.
# Example: Input: aaabbccccd Output: a3b2c4d1

string = input("Enter a string: ")
result = ""

if string:
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            result += string[i - 1] + str(count)
            count = 1
    result += string[-1] + str(count)

print(result)
