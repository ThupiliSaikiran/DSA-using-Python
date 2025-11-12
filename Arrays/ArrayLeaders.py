def leaders( arr):
        l=len(arr)-1
        maxx=0
        res=[]
        for i in range(l,-1,-1):
            if arr[i]>=maxx:
                res.append(arr[i])
                maxx=arr[i]
        return reversed(res)