def isIsomorphic(s,t):
  n=len(s)
  s_index_mp={}
  t_index_mp={}
  for i in range(n):
      if s[i] not in s_index_mp:
          s_index_mp[s[i]]=i
      if t[i] not in t_index_mp:
          t_index_mp[t[i]]=i
      if s_index_mp[s[i]] != t_index_mp[t[i]]:
          return False
  return True


print(isIsomorphic("foo","bar"))