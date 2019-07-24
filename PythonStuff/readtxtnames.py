def main():
    name_set()
    name=input("Enter a name: ")
    print(add_name_set(name))
    

def name_set():
    file=open("C:/Users/XNOTE/AppData/Local/Programs/Python/Python35/Name.txt",'w')
    lines=file.writelines(name_set2(lines))
    
    file.close()

def name_set2(lines):
    for line in lines:
        set(line)
def add_name_set(name):
    file=open("C:/Users/XNOTE/AppData/Local/Programs/Python/Python35/Name.txt",'a')
    addedset=file.add(name)
    file.close()
    return addedset
    
main()
