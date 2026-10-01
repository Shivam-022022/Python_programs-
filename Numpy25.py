import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))
flat = arr.flatten()

print("Flattened array:", flat)
print("\nElements greater than 50:", flat[flat > 50])
print("Even numbers:", flat[flat % 2 == 0])

average = np.mean(flat)
print("\nAverage value:", average)
print("Elements less than average:", flat[flat < average])
