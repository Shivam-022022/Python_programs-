# String Compression
# Compress repeated characters and return the original string if compression does not reduce the length.

string = input("Enter a string: ")
compressed = ""

if string:
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            compressed += string[i - 1] + str(count)
            count = 1
    compressed += string[-1] + str(count)

if len(compressed) < len(string):
    print(compressed)
else:
    print(string)
