import numpy as np

# A is 2x3 and B is 3x2, so they are compatible for multiplication
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

print("Matrix A (2x3):\n", A)
print("Matrix B (3x2):\n", B)
print("\nMatrix Multiplication (A x B):\n", np.dot(A, B))
# Alternatives: np.matmul(A, B) or A @ B
