import numpy as np

arr = np.random.rand(3, 4, 5)
print("Random 3D array (3x4x5):\n", arr)

print("\nMean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
