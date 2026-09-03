# Write a recursive function to search for an element in a sorted list using
# binary search.

def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)


if __name__ == "__main__":
    sorted_list = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
    target = 23
    index = binary_search(sorted_list, target)
    print(f"List: {sorted_list}")
    if index != -1:
        print(f"{target} found at index {index}")
    else:
        print(f"{target} not found in the list")
