import numpy as np

arr = np.arange(1, 28).reshape(3, 3, 3)
flat = arr.flatten()

print("3D array:\n", arr)
print("\nFlattened array:", flat)
print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))
