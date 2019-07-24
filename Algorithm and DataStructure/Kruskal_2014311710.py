G=[['A','B',8],
   ['A','C',14],
   ['B','E',11],
   ['B','D',9],
   ['C','D',5],
   ['D','F',12],
   ['D','E',13],
   ['E','F',8],
   ['E','G',8],
   ['F','G',7]]

S=[]

#reorder the Edges
for i in range(len(G)):
    idx=i
    for j in range(i+1,len(G)):
        if G[idx][2]>G[j][2]:
            idx=j
    G[i],G[idx]=G[idx],G[i]
        
#put in S
S.append(G[0][0:2])
#starting from the 2nd graph, seak each edges
for i in range(1,len(G)):
    #marking for if it is already inside Solution
    #to prevent cycle
    done=False
    #if both elements of the new edge is in one of the solution lists
    for j in range(len(S)):    
        if G[i][0] in S[j] and G[i][1] in S[j]:
            done=True
    #only append solution of else
    if not done:
        S.append(G[i][0:2])
   
    #check if our new solution list can be combined
        
    for k in (range(len(S)-1)):
        if len(S)-1==k:
                  continue
        #if our new solution list has any element in previous solution lists
        if any(elem in S[-1] for elem in S[k]):
            #combine them and empty the new solution list
            S[k]=S[k]+S[-1]
            S[-1]=[]
            #in case that combined solution list can be combined with another one
            #because our first new solution list can also have combined another list
            #before the list we found above
            for l in range(len(S)):
              if l==k:
                  continue
              if any(elem in S[k] for elem in S[l]):
                  S[k]=S[k]+S[l]
                  S[l]=[]
        
#erase our empty lists
for p in range(len(S)):
            if S[-1]==[]:
                del S[-1]

                
print(S)
