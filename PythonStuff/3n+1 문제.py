def collatz_num(num):
    tlist=[]

    while num>1:
        if num %2==0:
            num= num/2
        else:
            num=3*num+1
    return tlist

n=int(input("Enter"))
print(collatz_num(num))
