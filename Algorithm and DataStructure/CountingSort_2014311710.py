A=[1, 1, 3, 3, 3, 2, 2, 5, 2, 1]
B=[]
C=[]
n=len(A)
for i in range(n):
    B.append(0)

def countingSort(A,B,n): #B is the newList

    for i in range(0,max(A)+1): #C is a countingList
        C.append(0)
        
    for j in range(0,n-1): #amount of values that equal i
        C[A[j]]=C[A[j]]+1
       

    for k in range(1,max(A)+1): #summing to the right
        C[k]=C[k]+C[k-1]

    for l in reversed(range(0,n)): #put it in B
        B[C[A[l]]]=A[l]
        
        C[A[l]]=C[A[l]]-1
        
        

countingSort(A,B,n)
print(B)
