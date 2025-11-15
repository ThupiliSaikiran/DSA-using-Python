def noOfSubArrayWithSumK(arr,k):
  prefixSum=0
  count=0
  mp={0:1}
  n=len(arr)
  for i in range(n):
    prefixSum+=arr[i]
    rem=prefixSum-k
    if rem not in mp:
      mp[prefixSum]=mp.get(prefixSum,0)+1
    else:
      count+=mp[rem]
      mp[prefixSum]=mp.get(prefixSum,0)+1
  return count

print(noOfSubArrayWithSumK([1,1,1],2))

