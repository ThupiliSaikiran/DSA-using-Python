def removeOuterParentheses(s):
        n=len(s)
        string=""
        count=0
        for i in range(n):
            if s[i]=="(":
                count+=1
                if count > 1:
                    string+=s[i]
            else:
                count-=1
                if count >=1:
                    string+=s[i]
        return string


     


print(removeOuterParentheses("(()())(())"))