import numpy as np

# Try it yourself
a = np.array([10, 2, 30, 40, 50])
a[1] = 20
print(a)

# Print the even elements in the given array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:8:2])

# Find the size ,dimension and shape for the given array b
b = np.array([10, 20, 30, 40, 50, 60, 70])
print(b.size)
print(b.ndim)
print(b.shape)

# Find the sum of maximum and minimum value in the given numpy array
c = np.array([-10, 201, 43, 94, 502])
max_c = c.max()
min_c = c.min()
print(max_c + min_c)

# Perform addition, multiplication, division and subtraction operations on the given numpy array arr1 and arr2:
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr3 = np.add(arr1, arr2)
arr4 = np.subtract(arr1, arr2)
arr5 = np.multiply(arr1, arr2)
arr6 = np.divide(arr1, arr2)
print(arr3)
print(arr4)
print(arr5)
print(arr6)



