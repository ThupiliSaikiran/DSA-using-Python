
"""
#Array with array module

import array as myarray

arr=myarray.array('i',[10,20,30,40,50])

print(arr)
print(arr.typecode)
print(arr[0])
print(len(arr))



# add elements to the array
arr.append(10)
print(arr)

arr.insert(0,100)
print(arr)

#update array

arr[1]=1000
print(arr)




#removing elements
print(arr)
print(arr.pop(3))
print(arr)


print(arr)
print(arr.remove(4))
print(arr)


#slicing
print(arr[2:4])
print(arr[-4:-1])




#searching elements
print(arr)
print(arr.index(20))


#sorting

sorted_array=arr.tolist()
sorted_array.sort() #Ascending Order
print(sorted_array)
sorted_array.sort(reverse=True)  #Descending Order
print(sorted_array)


"""
import numpy as np

arr = np.array([12,21,46,90,34])
zeroes = np.zeros((2,2))
ones = np.ones((2,2))
const = np.full((3,3),0)
eye = np.eye(4)
random = np.random.random((3,3))

print(arr)
print("\n")
print(zeroes)
print("\n")
print(ones)
print("\n")
print(const)
print("\n")
print(eye)
print("\n")
print(random)

arr1=np.array([10,20,50,30],ndmin=4)
print(arr1)