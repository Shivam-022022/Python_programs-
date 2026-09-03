# Store 15 integers in a list. Count how many numbers are:
# • Even
# • Odd

numbers = [12, 7, 24, 15, 8, 31, 42, 19, 10, 27, 6, 33, 18, 21, 4]
even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
