import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)
flat = arr.flatten()

print("Original 3D array:\n", arr)
print("\nFlattened array:", flat)
