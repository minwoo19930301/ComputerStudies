A=[3,31,48,73,8,11,20,29,65,15] #initialize


def insertionSort(A):  #function

    for i in range(1,len(A)): #i repeats from 1 to 10
          x=i-1                     #x for indexing a position
          newItem=A[i]       #temperary value to get the index value
          
    # from below, this will sort the left side of the newItem by inserting
    
          while (newItem<A[x]): #shift only if newItem is smaller
              A[x+1]=A[x]
              x=x-1
              if x>=0:
                  break
          A[x+1]=newItem            #newItem stays if still x if i-1 
          
    return A
    
print(A)
print(insertionSort(A))
