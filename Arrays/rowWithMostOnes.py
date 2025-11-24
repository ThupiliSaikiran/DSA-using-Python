import numpy as np

def rowWithMostOnes(matrix):
  rows=len(matrix)
  cols=len(matrix[0])

  max_row_index=-1
  col = cols-1

  for row in range(rows):
    while col >=0 and matrix[row][col]==1:
      max_row_index=row
      col -=1
  return max_row_index

matrix=np.array([[0,0,1,1,1],[0,0,0,0,1],[0,1,1,1,1]])

print(rowWithMostOnes(matrix))