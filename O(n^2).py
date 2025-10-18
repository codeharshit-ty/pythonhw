def ONSquareTime(n):
    iteration =0
    for i in range(0,n):
          for j in range(0,n):
               print("*",end=" ")
               iteration+=1
          print("")
    print ("\nwhen n is ",n,"Iteration= ",iteration,"\n")

ONSquareTime(5)
ONSquareTime(4)
ONSquareTime(3)

print("\n when every 'n' the time taken equal n^2")
print("O(n^2)")