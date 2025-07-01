import numpy as np
arr3d = np.arange(2*3*4).reshape(2, 3, 4)
moved = np.moveaxis(arr3d, 0, -1)
print("Original shape:", arr3d.shape)
print("Moved shape:", moved.shape)
