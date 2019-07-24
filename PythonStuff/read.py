def main():
    new_name=input("Enter a Name: ").capitalize()
    lines=[]
    file_reader()
    print(add_dict(new_name))
    print(file_reader())

def file_reader():    
    global lines
    infile=open("C:/Users/XNOTE/AppData/Local/Programs/Python/Python35/Name.txt",'r')
    lines=infile.readlines()
    for line in lines:
        line=line.rstrip()        
    infile.close()

def add_dict(name):
    outfile=open("C:/Users/XNOTE/AppData/Local/Programs/Python/Python35/Name.txt",'a')
    global lines
    copy=outfile.writelines(lines)
    namelist=[]
    for line in lines:
        line=line.rstrip()
        namelist=namelist.append(line)
    updated=set(namelist).add(name)
    outfile.close()
    return list(updated).sort()


main()
