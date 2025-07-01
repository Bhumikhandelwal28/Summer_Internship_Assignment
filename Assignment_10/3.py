import numpy as np

arr = np.array([[1, np.nan, 3],
                [4, 5, np.nan]])
print("Original array\n",arr)

col_mean = np.nanmean(arr, axis=0)
arr=np.nan_to_num(arr,copy=True,nan=col_mean)

print("Updated array:\n", arr)
