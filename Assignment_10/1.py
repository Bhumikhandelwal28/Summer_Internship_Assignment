import numpy as np
arr=np.array([[6,-8,73,-110],[np.nan,-8,0,94]])
print(arr)
#replacing missing values
array=np.nan_to_num(arr,copy=True,nan=0.0)
print("Array after replacing NAN :\n",array)
array = np.pad(array, ((0,2), (0,0)), constant_values=0)
print(array)
#Interchange of rows
array[[0, 2]] = array[[2, 0]]
array[[1, 3]] = array[[3, 1]]
print(array)
array[:,[0, 2]] = array[:,[2, 0]]
array[:,[1, 3]] = array[:,[3, 1]]
print("Interchanged 2D array:\n", array)
