def isAnagram( s, t):
        if len(s)!=len(t):
            return False
        sorted_s="".join(sorted(s))
        sorted_t="".join(sorted(t))
        for i in range(len(s)):
            if sorted_s[i]!=sorted_t[i]:
                return False
        return True


def isAnagram1(s,t):
     if len(s) != len(t):
          return False
     res=[0]*26
     for i in range(len(s)):
          res[ord(s[i])-ord('a')]+=1
     for i in range(len(t)):
          res[ord(t[i])-ord('a')]-=1
     for i in res:
          if i != 0:
               return False
     return True

print(isAnagram1("rat","car"))