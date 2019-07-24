file1 = "tents.csv"
file2 ="students.csv"
file3 = "write.csv"

infile = open(file1,'r')
datalist=[]
for line in infile:
    print(line)
    datalist.append(line.strip())
    print("------------------",datalist)
for i in range(len(datalist)):
    datalist[i]=list(eval(datalist[i]))
infile.close()
print(datalist)
