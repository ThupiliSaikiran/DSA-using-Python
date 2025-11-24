def pattern7(n) :
    for i in range(n):
        for j in range(1,n-i):
            print(" ",end=" ")
        for k in range(2*i+1):
            print("*", end=" ")
        for j in range(1,n-i):
            print(" ",end=" ")
        print()
def pattern8(n):
  for i in range(n):
    for j in range(i):
      print(" ",end=" ")
    for k in range(2*n-(2*i+1)):
      print("*",end=" ")
    for l in range(i):
      print(" ",end=" ")
    print()




pattern7(5)
pattern8(5)