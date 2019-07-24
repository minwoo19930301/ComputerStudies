def main():
    name_set()
    name=input("Enter a name: ")
    print(add_name_set(name))
    

def name_set():
    file=open("Names.txt",'w')
    lines=file.writelines()
    for line in lines:
        set(line)        
    file.close()

def add_name_set(name):
    file=open("Names.txt",'a')
    addedset=file.add(name)
    file.close()
    return addedset
    
main()
