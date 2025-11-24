def longestConsecutiveSequence(arr):
  arr.sort()
  # print(arr)
  longest=1
  lastSmaller=-10**9
  count=0
  n=len(arr)
  for i in range(n):
    if arr[i]-1 == lastSmaller:
      count+=1
      lastSmaller=arr[i] 
    elif arr[i] != lastSmaller:
      count=1
      lastSmaller=arr[i]
    longest=max(count,longest)
    
   
  return longest

# print(longestConsecutiveSequence([100,101,100,101,101,4,3,2,3,2,1,1,1,2]))


def longestConsecutiveSequence1(arr):
  n=len(arr)
  longest=0
  se=set()
  for i in range(n):
    se.add(arr[i])

  for s in se:

    if s-1 not in se:
      count=1
      x=s
   
      while x+1 in se:
        count+=1
       
        x+=1
      longest=max(count,longest)
  return longest
  
print(longestConsecutiveSequence1([]))

