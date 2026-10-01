import numpy as np

arr = np.random.randint(1, 101, size=(2, 3, 4))
print("Original 3D array:\n", arr)

arr[arr > 50] = 0
print("\nAfter replacing values > 50 with 0:\n", arr)
