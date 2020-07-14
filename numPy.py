#############################################################################################
from numpy.random import randint # import certain function
# NumPy Arrays
# Cast normal array to np array
my_list = [1,2,3]
import numpy as np 
arr = np.array(my_list)
print(arr)

my_mat = [[1,2,3], [4,5,6], [7,8,9]]
print(np.array(my_mat))

# Generate array in np
# arange(start, end, steps)
print(np.arange(0, 10, 2)) 

# Generate zero
# np.zeros((rows, columns))
print(np.zeros((2, 3)))
# Generate ones
print(np.ones((4,5))) 

# Arithmetic sequence 
print(np.linspace(0, 5, 10))

# matrix with 1
print(np.eye(4))

# Generate random number or matrix
print(np.random.rand(5, 5)) # 5 by 5 matrix random nums

# Standard normal distribution
print(np.random.randn(2, 2)) 

# Random int with min and not included max
print(np.random.randint(1, 100, 10))

arr = np.arange(25)
print(arr.reshape(5,5)) # reshape allow reshape(row, col)
ranarr = np.random.randint(0,50,10)

# Max, Min, Index
print(ranarr.max(), ranarr.min(), ranarr.argmax(), ranarr.argmin())

# shape
print(arr.shape)
print(arr.reshape(5,5).shape)

# datatype
print(arr.dtype)

#############################################################################################
arr = np.arange(0, 11)
print(arr[1:5], arr[:6], arr[0:5], arr[5:])
slice_of_array = arr[0:6]
print(slice_of_array)
slice_of_array[:] = 99 # This will influence the original array. 
# Python does not copy!!! 
# If you want to copy
arr_copy = arr.copy()
print(arr_copy)


















