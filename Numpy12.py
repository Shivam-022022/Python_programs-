import numpy as np

arr = np.array([12, 75, 33, 91, 50, 64, 8, 100, 49, 55])
print("Original array:", arr)

arr[arr > 50] = 0
print("After replacing elements > 50 with 0:", arr)
