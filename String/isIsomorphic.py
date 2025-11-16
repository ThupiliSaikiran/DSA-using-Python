def isIsomorphic(s,t):
  n=len(s)
  mp={}
  for i in range(n):
    if s[i] in mp:
      if mp[s[i]] != t[i]:
        return False
    else:
      mp[s[i]]=t[i]
  return True


