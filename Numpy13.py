import numpy as np

arr = np.array([45, 12, 78, 23, 56, 9, 34, 67])
print("Unsorted array:", arr)

print("Ascending order:", np.sort(arr))
print("Descending order:", np.sort(arr)[::-1])
