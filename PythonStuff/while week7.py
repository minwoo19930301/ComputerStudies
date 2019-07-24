#2014311710 Kim Minwoo

#1
n=int(input("Enter a integral for a factorial: "))
a=1
s=1
if n<=0:
           print("error")
else:
    while a<=n:
        s=s*a
        a=a+1
    print(s,"\n")

#2
s=0
print("Enter numbers to add to the sum. \nEnter 0 to quit \nCurrent Sum:"+str(s))
n=eval(input("Number?:"))

while n!=0 :
        s=s+n
        print("Current Sum:"+str(s))
        n=eval(input("Number?:"))
print("Current Sum:"+str(s))               
