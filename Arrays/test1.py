""" Longest sub array with sum K with only positive Integers"""

#Better
def longSubArr(arr,k):
  maxLen=0
  preSum=0
  mp={}
  for i in range(len(arr)):
    preSum+=arr[i]
    if preSum == k:
      maxLen=i+1
    rem=preSum-k
    if rem in mp:
      length=i-mp[rem]
      maxLen=max(length,maxLen)
    if rem not in mp:
      mp[preSum]=i

  return maxLen



def longSubArrOptimal(arr,k):
  n=len(arr)
  i,j =0,0
  S=arr[0]
  maxLen=0
  while j<n:
    while i <= j and S>k:
      S-=arr[i]
      i+=1
    if S==k:
      maxLen=max(maxLen,j-i+1)
    j+=1
    if j < n:
      S+=arr[j]
    
  return maxLen



print(longSubArrOptimal([1,2,3,1,1,1,1,3,3],3))
