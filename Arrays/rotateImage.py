def rotateImage(arr):
  n=len(arr)
  m=len(arr[0])
  for i in range(n-1):
    for j in range(i+1,m):
      arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
  for i in range(n):
    arr[i].reverse()
  return arr
      
    
  
 
    


print(rotateImage([[1,2,3],[4,5,6],[7,8,9]]))