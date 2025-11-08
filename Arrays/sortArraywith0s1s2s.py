def sortArr(arr):
  n=len(arr)
  count0=0
  count1=0
  count2=0

  for i in range(n):
    if arr[i]==0:count0+=1
    elif arr[i]==1:count1+=1
    else:count2+=1

  for i in range(count0):
    arr[i]=0
  for i in range(count0,count0+count1):
    arr[i]=1
  for i in range(count0+count1,n):
    arr[i]=2
  return arr


#Dutch National Flag Algorithm (DNF)

def sortColors(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        low=0
        mid=0
        high=n-1
        while mid <= high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        return nums

print(sortColors([0,1,1,0,1,2,1,2,0,0,0]))