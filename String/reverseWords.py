def reverseWords(s):
  sList=s.split()
  n=len(sList)
  left=0; right=n-1
  print(left,right)
  while left < right:
    sList[left],sList[right]=sList[right],sList[left]
    left+=1
    right-=1
  return " ".join(sList)
    
    

def reverseWords1(s):
  n=len(s)
  left=0; right=n-1
  temp=""
  res=""
  while left <= right:
    st=s[left]
    if st != " ":
      temp+=st
    else:
      if res != "":
        res=temp+" "+res
      else:
        res=temp
      temp=""
    # print(res)
    left+=1
  if temp !="":
    if res != "":
        res=temp+" "+res
    else:
      res=temp
  return res
    
  
 










print(reverseWords("a good   example"))