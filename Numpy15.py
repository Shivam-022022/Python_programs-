import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([[7, 8, 9],
              [10, 11, 12]])

print("Array a:\n", a)
print("Array b:\n", b)

print("\nHorizontal concatenation:\n", np.hstack((a, b)))
print("\nVertical concatenation:\n", np.vstack((a, b)))
