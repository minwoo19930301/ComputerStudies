#2014311710 Kim Minwoo
#Although I am aware of the fact that this list is not
#calling by reference. whereas calling by value,
#the assignment requested to not use class,
#so I reluctantly used arrays....


#the arrays are set as [0] : the link of prev. [1] : the value, [2]: the next link
def insert(value):
    newNode=[None,value,None]
    newNode[0]=tail[0]
    newNode[2]=tail
    tail[0][2]=newNode
    tail[0]=newNode
    
def printList(start):
    while start[2][2]!=None:
        start=start[2] 
        print(start[1])

def delete(value):
    delNode=head
    while delNode:
        if delNode[1]==value:
            delNode[0][2]=delNode[2]
            delNode[2][0]=delNode[0]
            del delNode
            break
        delNode=delNode[2]
        
#main
head=[None,None,None]
tail=[None,None,None]
head[2]=tail
tail[0]=head
insert(2)
insert(1)
insert(5)
insert(6)
insert(8)
printList(head)
delete(8)
delete(6)
delete(5)
delete(1)
delete(2)
printList(head)
