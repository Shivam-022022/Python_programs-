# Problem Statement:
# Display all employee information.
# Store item prices in a tuple and calculate:
# Total bill
# Average price

# Answer:
temperatures = (32, 35, 31, 36, 34, 33, 30)

total = sum(temperatures)
maximum = temperatures[0]
minimum = temperatures[0]

for temperature in temperatures:
    if temperature > maximum:
        maximum = temperature
    if temperature < minimum:
        minimum = temperature

average = total / len(temperatures)

print("Maximum temperature:", maximum)
print("Minimum temperature:", minimum)
print("Average temperature:", average)
