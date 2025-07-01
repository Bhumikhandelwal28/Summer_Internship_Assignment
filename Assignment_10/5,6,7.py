import numpy as np
from scipy import stats

arr1=np.array([3,4])
arr2=np.array([1,0])
avg=(arr1+arr2)/2
print("Average of Numpy Arrays:\n",avg)

arr= np.array([[11, 24], [36, 49]])

mean=np.mean(arr)
print("Mean of two numpy arrays is:\n",mean)
avg=np.average(arr)
print("Average of two numpy arrays is:\n",avg)
median=np.median(arr)
print("Median of two numpy arrays is:\n",median)

mode_result = stats.mode(arr, axis=None, keepdims=False)
print("Mode:", mode_result.mode)
print("Frequency:", mode_result.count)
