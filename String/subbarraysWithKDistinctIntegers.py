def at_most_k_distinct(arr,k):
        left=0;res=0
        freq={}
        for right in range(len(arr)):
            freq[arr[right]]=freq.get(arr[right],0)+1
            
            while len(freq)>k:
                freq[arr[left]]-=1
                if freq[arr[left]]==0:
                    del freq[arr[left]]
                left+=1
            res+=(right-left+1)
        return res
    
def exactlyK(arr, k):
        return at_most_k_distinct(arr,k) - at_most_k_distinct(arr,k-1)