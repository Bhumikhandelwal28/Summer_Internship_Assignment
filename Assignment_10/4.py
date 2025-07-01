import numpy as np
arr = np.array([[4, -3, 2], [-1, -6, 5]])
arr[arr < 0] = 0
print("Negative values replaced with 0:\n", arr)
