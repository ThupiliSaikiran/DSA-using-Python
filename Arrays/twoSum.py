def twoSum(arr,target):
  n=len(arr)
  mp = {}
  for i in range(n):
    rem=target-arr[i]
    if rem in mp:
      return [mp[rem],i]
    else:
      mp[arr[i]]=i
  return     


print(twoSum([2,6,5,8,11],14))
     

