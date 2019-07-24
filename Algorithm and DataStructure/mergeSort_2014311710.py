def mergeSort(A):
    #divide if not single elements
    if(len(A)>1):
        #the middle
        middle=len(A)//2
        #make two divided lists on the criteria of middle
        left=[]
        right=[]
        for i in range(middle):
            left.append(A[i])
        for j in range(middle,len(A)):
            right.append(A[j])
        
        #recursively divide
        mergeSort(left)
        mergeSort(right)

        #iteratively merge starting from the divided lists
        i=0
        j=0
        k=0

        #loop
        while 1:
            #if there is both left and rights to compare
            if i<len(left) and j<len(right):
                if left[i]<right[j]:
                    A[k]=left[i]
                    i+=1
                else:
                    A[k]=right[j]
                    j+=1
                k+=1

            #if only the left side is left
            if i < len(left) and j==len(right):
                A[k]=left[i]
                i+=1
                k+=1
            #if onlt the right side is left
            if i==len(left) and j<len(right):
                A[k]=right[j]
                j+=1
                k+=1
            #break loop if no more to compare
            if i==len(left) and j==len(right):
                break

A=[5,3,1,4,2]
print(A)
mergeSort(A)
print(A)
