import numpy as np
A = np.array([[1, -2, 3],
              [-1, 3, -1],
              [2, -5, 5]])
B = np.array([9, -6, 17])

sol = np.linalg.solve(A, B)
print("Solution using linalg.solve():", sol)

A_inv = np.linalg.inv(A)
sol2 = np.dot(A_inv,B)
print("Solution using inverse method:", sol2)
