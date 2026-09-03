# Create a dictionary of cities and their populations. Remove a specified
# city from the dictionary.

def remove_city(city_dict, city):
    city_dict.pop(city, None)
    return city_dict


if __name__ == "__main__":
    cities = {"Mumbai": 12442373, "Delhi": 11007835, "Kolhapur": 549236, "Pune": 3124458}
    print(f"Original: {cities}")

    updated = remove_city(cities, "Delhi")
    print(f"Updated: {updated}")
