
f=open("C:/Users/XNOTE/AppData/Local/Programs/Python/Python35/Name.txt",'a')
f.write("\n")
name=input("enter name: ").capitalize()
f.write(name+"\n")
f.close()

o=open("C:/Users/XNOTE/AppData/Local/Programs/Python/Python35/Name.txt", 'r')
data=o.readlines()
data=sorted(list(set(data)))

p=open("C:/Users/XNOTE/AppData/Local/Programs/Python/Python35/Name.txt",'w')
p.writelines(data)
o.close()
p.close()
