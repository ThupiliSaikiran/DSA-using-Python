def nextPermutation(arr):
  n=len(arr)
  index=-1
  for i in range(n-2,-1,-1):
    if arr[i]<arr[i+1]:
      index=i
      break
  if index==-1:
    return arr.reverse()
  
  
  for i in range(n-1,i+1,-1):
    if arr[index]<arr[i]:
      arr[index],arr[i]=arr[i],arr[index]
      break
  arr[index+1:]=reversed(arr[index+1:])
  return arr

print(nextPermutation([2,1,5,4,3,0,0]))