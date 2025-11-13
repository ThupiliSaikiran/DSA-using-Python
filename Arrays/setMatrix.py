def setMatrix(arr):
  rowsLength=len(arr)
  columnLength=len(arr[0])
  rows=[0]*rowsLength
  cols=[0]*columnLength
  for i in range(rowsLength):
    for j in range(columnLength):
      if arr[i][j]==0:
        rows[i]=1
        cols[j]=1

  for i in range(rowsLength):
    for j in range(columnLength):
      print(rows[i],cols[j])
      if rows[i]==1 or cols[j]==1:
        arr[i][j]=0
  return arr
      

def setZeroes(matrix):
       m=len(matrix)
       n=len(matrix[0])
       col0=1
       for i in range(m):
        for j in range(n):
            print(matrix[i][j])
            if matrix[i][j]==0:
                matrix[i][0]=0
                if j != 0:
                    matrix[0][j]=0
                else:
                    col0=0
       for i in range(1,m):
          for j in range(1,n):
             if matrix[i][j]!=0:
                if matrix[i][0]==0 or matrix[0][j]==0:
                   matrix[i][j]=0
       if matrix[0][0]==0:
          for j in range(1,n):
             matrix[0][j]=0
       if col0 == 0:
          for i in range(m):
             matrix[i][0]=0
       return matrix
             
                   
             
   
              
      

        
     
print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))