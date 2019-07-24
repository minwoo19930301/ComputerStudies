while True:
    x=int(input("number"))
    a=1
    s=0
    while 1<=a<=x:
        a=a+1
        if x%a==0:
        
            s=s+a
    if s==x:
        print(x)
