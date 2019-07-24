list1=[]
while True:
    a=input()
    if a=="q":
        break
    elif int(a)>100:
        a="over"
    list1.append(a)
    

for i in range(len(list1)):
    print(list1[i])


