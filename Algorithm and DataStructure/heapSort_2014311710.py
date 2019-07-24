def heapify(A,k,n):

    left=2*k+1
    right=2*k+2
    larger=k
    if  right<=n-1:                             #if there is both left and right nodes
        if(A[left]<A[right]):
           larger=right
        else:
           larger=left
    elif left<=n-1:                              #if there is only left node
        larger=left
    else:                                         #if no child nodes return
        return
    
    if (A[larger]>A[k]):                  #if there is larger value in childnode, switch
        A[k],A[larger]=A[larger],A[k]
        heapify(A,larger,n)


def heapSort(B):
    for i in reversed(range(0,int((len(B)/2)))): #start with parent node that has the last children node
        heapify(B,i,len(B))
        
    for j in reversed(range(0,len(B))):
        B[j],B[0]=B[0],B[j]                 #switch the maximum(top) and end node
        heapify(B,0,j)                          #heapify again except the last node


def main():
    _list=[3,31,48,73,8,11,20,29,65,15]
    print(_list)
    heapSort(_list)
    print("------------heapsorted----------------")
    print(_list)
main()
