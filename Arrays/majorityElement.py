#Better
def majorityElement(arr):
  n=len(arr)
  mp={}
  for i in range(n):
    mp[arr[i]]=mp.get(arr[i],0)+1
  for i in mp:
    if mp[i]> n//2:
      return i
  return -1


#Best

def majorityElement(nums):
        n=len(nums)
        ele=None
        count=0
        for i in range(n):
            if count == 0:
                ele=nums[i]
                count+=1
            elif nums[i]==ele:
                count+=1
            else:
                count-=1
        res=0
        for i in range(n):
            if nums[i]==ele:
                res+=1
        if res > n//2:
            return ele
        return -1



arr=[2,2,1,3,1,1,3,1,1]

print(majorityElement(arr))
