import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D array:\n", arr)
print("\nNumber of dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
