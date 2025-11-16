def largestOddNumber(num):
        n=len(num)
        left=0;right=n-1
        while left <= right:
            if int(num[right])%2==1:
                return num[left:right+1]
            else:
                right-=1
        return ""
