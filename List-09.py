# Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.

cities = ["Pune", "Mumbai", "Nashik", "Kolhapur", "Nagpur"]
city = input("Enter city name: ")

if city in cities:
    print("City exists in the list")
else:
    print("City does not exist in the list")
