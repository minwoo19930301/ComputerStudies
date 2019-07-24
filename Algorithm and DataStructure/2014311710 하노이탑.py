#2014311710 김민우 


n=int(input("원반갯수: "))
A=[]
B=[]
C=[]
F=[]
x=0
y=0


for i in range(1,n+1):
    A.append(i) 

A.reverse()

print(A,B,C,F)


if max(A)!=A[-1]:
   
        for i in range(0,len(A)):
            if i%2==0:
                x=A[i]
            else:
                y=A[i]

        if A[-1]==y and (B==[] or A[-1]<B[-1]):
            B.append(A[-1])
            A.remove(A[-1])
            print(A,B,C
                  )
    
        elif A[-1]==x and (C==[] or A[-1]<C[-1]):
            C.append(A[-1])
            A.remove(A[-1])
            print(A,B,C)
        
        for i in range(0,len(A)):
            if i%2==0:
                x=A[i]
            else:
                y=A[i]

        if A[-1]==y and (B==[] or A[-1]<B[-1]):
            B.append(A[-1])
            A.remove(A[-1])
            print(A,B,C)
        
        elif A[-1]==x and (C==[] or A[-1]<C[-1]):
            C.append(A[-1])
            A.remove(A[-1])
            print(A,B,C)
    
        
        
if B!=[] or C!=[] or A[-1]>B[-1] and A[-1]>C[-1]:
        
        if B[-1]<C[-1] and len(B)<2:
            C.append(B[-1])
            B.remove(B[-1])
            print(A,B,C)
            
        elif B[-1]>C[-1] and len(C)<2:
            B.append(C[-1])
            C.remove(C[-1])
            print(A,B,C)
        
        else:
           
            for i in range(0,len(B)):
                
                if i%2==0:
                    x=B[i]
                else:
                    y=B[i]
            
            
            if B[-1]==y and (C==[] or B[-1]<C[-1]):
                C.append(B[-1])
                B.remove(B[-1])
                print(A,B,C)
                
            elif B[-1]==x and (A==[] or B[-1]<A[-1]):
                A.append(B[-1])
                B.remove(B[-1])
                print(A,B,C)
                
        if max(A)!=A[-1]:
   
            for i in range(0,len(A)):
                if i%2==0:
                    x=A[i]
                else:
                    y=A[i]

            if A[-1]==y and (B==[] or A[-1]<B[-1]):
                B.append(A[-1])
                A.remove(A[-1])
                print(A,B,C)
    
            elif A[-1]==x and (C==[] or A[-1]<C[-1]):
                C.append(A[-1])
                A.remove(A[-1])
                print(A,B,C)
                
        if B[-1]>C[-1]:
            for i in range(0,len(C)):
                if i%2==0:
                    x=C[i]
                else:
                    y=C[i]

            if C[-1]==y and (A==[] or A[-1]>C[-1]):
                A.append(C[-1])
                C.remove(C[-1])
                print(A,B,C)
    
            elif C[-1]==x and (B==[] or B[-1]>C[-1]):
                B.append(C[-1])
                C.remove(C[-1])
                print(A,B,C)
                
   
        else:
             C.append(A[-1])
             A.remove(A[-1])
             print(A,B,C)
        
                
else:
     F.append(A[-1])
     A.remove(A[-1])
     




