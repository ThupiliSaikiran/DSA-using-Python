arr1=[1,1,2,2,99,3,3,5,5,6,6]
n =6




def eleAppearOnce(arr1):
  mp={}
  for num in arr1:
    mp[num]=mp.get(num,0)+1

  for i in mp:
    if mp[i]==1:
      return i
        
  
print(MaximumConsecutiveOnes(arr1))
