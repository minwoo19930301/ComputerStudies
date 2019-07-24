f= open("grade.txt",'r')
lines=f.readlines()
a=[]
b=[]
for line in lines:
    b=line.split()
    a.append(b)
print(a)
f.close()
