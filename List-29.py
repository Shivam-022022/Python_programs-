# Store the temperature of 30 days and determine:
# • Hottest day
# • Coldest day
# • Average temperature
# • Days above average temperature
# • Days below average temperature

temperatures = []

for i in range(30):
    temperatures.append(float(input("Enter temperature: ")))

hottest = temperatures[0]
coldest = temperatures[0]
total = 0

for temperature in temperatures:
    if temperature > hottest:
        hottest = temperature
    if temperature < coldest:
        coldest = temperature
    total += temperature

average = total / len(temperatures)
above = 0
below = 0

for temperature in temperatures:
    if temperature > average:
        above += 1
    elif temperature < average:
        below += 1

print("Hottest day temperature:", hottest)
print("Coldest day temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above)
print("Days below average:", below)
