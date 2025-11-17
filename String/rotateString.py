def rotateString(s,goal):
        if len(s) != len(goal):
            return False
        doubleStr=s+s
        if goal in doubleStr:
            return True
        return False



s="ba"
s1=''.join(sorted(s))
print(s1)