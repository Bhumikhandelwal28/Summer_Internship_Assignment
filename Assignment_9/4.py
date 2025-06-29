import numpy as np
arr=np.array([[23,45,67],[44,87,32]])

#accessing the maximum element
max_e=arr.max()
print(max_e)
#accessing the minimum element
min_e=arr.min()
print(min_e)

#accessing rows and columns
row,col=np.shape(arr)
print("Rows:",row,"Columns:",col)

#selecting elememt
for i in arr:
    print(i)
    for element in i:
        print(element)

#selecting particular element
ele=arr[1][2]
print("The value at (2,3) in the array is :",ele)

#Finding sum of all elements in the array
sumi=0
for i in arr:
    for j in i:
        sumi=sumi+j

print("The sum of all elements:",sumi)

#Adding,Subtraction,Multiply,Division of array
a=np.array([[1,2,3],[4,5,6],[3,4,5]])
b=np.array([[10,11,12],[13,14,15],[2,4,7]])
print("Addition of two array:",a+b)
print("Subtraction of two array:",a-b)
print("Multiplication of two array:",a*b)
print("Division of two array:",a/b)