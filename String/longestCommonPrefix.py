def longestCommonPrefix(strs):
  strs.sort()
  n=len(strs)
  first=strs[0]
  last=strs[-1]
  res=[]
  for  i in range(min(len(first),len(last))):
    if first[i]!=last[i]:
      return "".join(res)
    else:
      res.append(first[i])
   
  
  return "".join(res)
  





print(longestCommonPrefix(["flower","flow","flight"]))