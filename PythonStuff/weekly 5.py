#2014311710 Minwoo Kim

#1
for i in range(1,6):
    print("*" *(2*i-1))

#2
for i in range(1,10):
    for j in range(1,10):
        print("%4d" %(i*j), end=(""))
    print() 

#3
a=int(input("type an integral for ASCII art N: "))
if a ==1:
    print("N")
else:
    for i in range (a):
        x=list(" "*(a))
        x[0]='N'
        x[a-1]='N'
        x[i]='N'
        print("".join(x))
        
        
        
