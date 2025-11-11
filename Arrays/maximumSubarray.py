#Better

def maxSubArray(nums):
        n=len(nums)
        maximum=-10**4
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                maximum=max(maximum,s)
        return maximum

def maxSubArray1(arr):
     n=len(arr)
     maximum=-10**4
     ansStart=-1
     ansEnd=-1
     s=0
     for i in range(n):
          if s == 0:
               start=i
          s+=arr[i]
          if s > maximum:
               maximum=s
               ansStart=start
               ansEnd=i
          if s<0:
               s=0
     return maximum

print(maxSubArray1([-2,-3,4,-1,-2,1,5,-3]))
        
      
          