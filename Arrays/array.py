#1. Largest element in an array

#Brute force is sort the array in the sorting , print(n-1)
#TC => O(nlogn)
#SSSC => O(1)

#optimal
n=5
arr = [1,20,3,4,5]

largest=arr[0]
for i in range(1,n):
  if arr[i]>largest:
    largest = arr[i]

print(largest)

#----------------------------------------------------

"""
2.Second largest Element in an array without sorting

sorting takes time => O(nlogn)
Brute Force:
-------------
Brute force is sort the array and search from the n-1 to find the second largest so here , 
for sort TC => O(nlogn)
for search TC => O(n)
Overall TC => nlogn+n

Better :
--------
first we traverse through the array find the first largest -> TC => O(N)
second we traverse again now here initial sl = -1 and then check the condition , the element is greater than sl and less than first largest -> TC => O(N)
Overall TC => O(N)+O(N)=O(2N)

"""

#Optimal
n=5
arr = [1,20,3,4,5]

largest = arr[0]
secondLargest = -1

for i in range(n):
  if arr[i]>largest:
    secondLargest= largest
    largest = arr[i]
  elif arr[i]< largest and arr[i] > secondLargest:
    secondLargest=arr[i]

print(secondLargest)

#Second smallest
#-----------------#

smallest = arr[0]
secondSmallest = 2**31-1

for i in range(n):
  if arr[i]<smallest:
    secondSmallest=smallest
    smallest=arr[i]
  elif arr[i]>smallest and arr[i] < secondSmallest:
    secondSmallest=arr[i]

print(secondSmallest)




"""
3.Check the given array is sorted or not
"""

arr=[1,2,2,3,2,3,4]

def checkSort(arr):
  for i in range(1,len(arr)):
    if arr[i-1]<=arr[i]:
      continue
    else:
      return False
  return True

#print(checkSort(arr))

"""
4.Remove duplicates in-place from sorted array
arr = [1,1,2,2,2,3,3]
o/p = [1,2,3,_,_,_,_]
Brute force:
------------
create set and add each element but set doesn't contain any duplicates, then traverse the set and replace it in the arr
"""

#-----Brute Force -----#
arr = [1,1,2,2,2,3,3]

s = set()

for i in range(len(arr)):
  s.add(arr[i])

index=0
for i in s:
  arr[index]=i
  index+=1

#print(index)

#TC => O(nlogn) + O(n)
#SC => O(N)

#-------Optimal-----#
arr = [1,1,2,2,2,3,3]

i=0
for j in range(1,len(arr)):
  if arr[i] != arr[j]:
    arr[i+1]=arr[j]
    i+=1
print(i+1)

#TC => O(N)
#SC => O(1)