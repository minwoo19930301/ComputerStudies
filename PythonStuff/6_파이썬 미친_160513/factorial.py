num=int(input("Enter a number"))

def factorial(num):
    fac=1
    for i in range(1,num+1):
        fac=i*fac
        
    return fac

print("%d! is %d" %(num,factorial(num)))
