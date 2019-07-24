#2014311710 Kim Minwoo

    
def main():
    global file
    file="C:/Users/XNOTE/AppData/Local/Programs/Python/Python35/Name.txt"
    new_name=input("Enter a Name: ").capitalize()+"\n"
    adder(new_name)
    reader()
    
def adder(name):

#append and set it, then alphabetically sort it by lists
    outfile=open(file,'a+')
    outfile.writelines("\n"+name)
    outfile.seek(0)
    lines=sorted(list(set(outfile.readlines())))
    outfile.close()

#rewrite the file
    outfile=open(file,'w')
    outfile.writelines(lines)
    outfile.close()
    
    return

def reader():

    infile=open(file,'r')
    lines=infile.readlines()
    for line in lines:
        line=line.rstrip()
        print(line)
    infile.close()

main()
