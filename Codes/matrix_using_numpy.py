from numpy import *
arr1 = array([
              [1,2,3,4,5,6],
              [3,4,7,8,2,9]
              ])
print(arr1.ndim) #give the dimension of array
print(arr1.dtype) #returns the data type used in array
print(arr1)

arr2 = arr1.flatten() #converts n dimesional to 1 dimensional
print(arr2)

arr3 = arr2.reshape(3,4) #converts 1D to 2D
print(arr3.ndim)

arr4 = arr2.reshape(2,2,3) #converts 1D to 3D
print(arr4.ndim)
print(arr4[0][1][1])

m = matrix(arr1) #creating matrix because it has more attributes which we can use
print(diagonal(m))
print(m.max())

#multiplying the matrices
m1 = matrix('1 2 3; 6 4 5; 1 6 7')
m2 = matrix('1 2 3; 6 8 5; 1 6 7')
m3 = m1 + m2
m4 = m1 * m2
print(m3)
print(m4)