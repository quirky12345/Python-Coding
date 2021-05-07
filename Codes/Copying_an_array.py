#adding 5 to all the elements of integer array

from numpy import *
# arr = array([1,2,3,4,5])
# arr = arr+5
# print(arr)

#adding two different array: vectorized operation

# arr1 = array([1,2,3,4,5])
# arr2 = array([1,3,5,2,10])
# arr3 = arr1 + arr2
# print(arr3)

#print sin/cos/log/sum/min of array

# arr1 = array([1,2,4,3,5])
# print(sort(arr1))

#concatenate two array

# arr1 = array([1,2,3,4,5])
# arr2 = array([1,3,5,2,10])
# print(concatenate([arr1,arr2]))

#copy the array

#here both array will be pointing to same memory reference
# arr1 = array([1,2,3,4,5])
# arr2 = arr1.view()
# print(id(arr2))

#shallow copy: if you try to change the content of one array it will impact other as well
#this means they are interlinked. Although they are pointing to different memory reference
# arr1 = array([1,2,3,4,5])
# arr2 = arr1
# print(id(arr2))

#deep copy: two different array which are not linked
arr1 = array([1,2,3,4,5])
arr2 = arr1.copy()
arr1[0] = 19
print(arr1)
print(arr2)
