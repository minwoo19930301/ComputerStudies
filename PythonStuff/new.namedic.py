new_name=input("Enter a Name: ").capitalize()

infile=open("C:/Users/XNOTE/AppData/Local/Programs/Python/Python35/Name.txt",'r')
lines=infile.readlines()
print(lines)
for line in lines:
    line=line.rstrip()
    print(line)

outfile=open("C:/Users/XNOTE/AppData/Local/Programs/Python/Python35/Name.txt",'a')
print(outfile)
print(lines)
print("///////////////////////////")
for line in lines:
    line=line.rstrip()
lines.append(new_name)
    
print(lines)
print("1111111111111111111111111111111111111111111111\n")
updated=set(lines)


print(updated)

infile.close()
outfile.close()

