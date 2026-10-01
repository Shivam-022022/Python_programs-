import numpy as np

arr = np.arange(1, 17).reshape(4, 4)
print("4 x 4 array:\n", arr)

print("\nFirst row:", arr[0])
print("Last column:", arr[:, -1])
print("Diagonal elements:", np.diagonal(arr))
print("Second and third rows:\n", arr[1:3])
