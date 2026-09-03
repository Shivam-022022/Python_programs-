# Create a set of cities and determine the total number of cities using
# an appropriate function.

def total_cities(city_set):
    return len(city_set)


if __name__ == "__main__":
    cities = {"Mumbai", "Delhi", "Kolhapur", "Pune", "Bengaluru"}
    print(f"Cities: {cities}")
    print(f"Total number of cities = {total_cities(cities)}")
