

f=open("Names.txt",'r')
for line in f:
    line=line[:-1]
    print(line)

f.close()
