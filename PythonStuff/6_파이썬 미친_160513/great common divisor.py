M= int(input("Enter value of M: "))
N= int(input("Enter value of N: "))
commons=[]

if (M==0) or (N==0):
    print("error")

    
for i in range(1,M+1):
    if M%i==0 and N%i==0:
       commons.append(i)
       
for i in range(1,N+1):
    if M%i==0 and N%i==0:
       commons.append(i)

print(max(commons))


    
