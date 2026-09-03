# Write a function that accepts a list and returns a new list containing only
# unique elements.

def unique_elements(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


if __name__ == "__main__":
    lst = [1, 2, 2, 3, 4, 4, 5, 1]
    print(f"List: {lst}")
    print(f"Unique elements = {unique_elements(lst)}")
