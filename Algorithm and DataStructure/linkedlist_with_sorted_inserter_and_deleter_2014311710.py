#2014311710 Minwoo Kim, SingleLinkedList with sorted inserter and deleter

class Node:                                                         #initializer
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):                                             #initializer
        self.head=Node(None)
        
    def insert(self,value):
        newNode=Node(value)
        if self.head.next==None:                            #if there is no list
            self.head.next=newNode                      #just put it next to head
        else:                                                     #if there is a list then find index first
            searcher=self.head
            if value<searcher.next.data:                # if smaller at first time this value is the smallest
                newNode.next=searcher.next
                self.head.next=newNode
            elif value>searcher.next.data:           #if not find the right sort
                while True:
                        searcher=searcher.next
                        
                        if searcher.next==None:
                            break
                        elif value<searcher.next.data:
                            break
                        elif value==searcher.next.data:     #if same number as in not minimum
                            return
        
                if searcher.next==None:                 #if last node put it in the last
                        searcher.next=newNode
                else:
                        newNode.next=searcher.next      #if not last link it in between
                        searcher.next=newNode
            else:
                print("E")
                return                                              #if same number as minimum

    def delete(self,value):
        searcher=self.head
        while value!=searcher.next.data:                #find value==searcher.next
            searcher=searcher.next
            if searcher.next==None:                         #if not found, ignore and return None
                return
        if searcher.next.next==None:                    #if found but last node, put previous node linked to null
            searcher.next=None
        else:                                                    #if found but in middle make the previous linked right to next
            searcher.next=searcher.next.next          
 
    def printList(self):                    
        cur=self.head                                       #cur as pointer
        curList=[]                                            #curList as a set of array
        while cur.next!=None:
                cur=cur.next                                #append list until end
                curList.append(cur.data)
        print(curList)


class Main:
    
    linkedList1=LinkedList()                                        # initialize
    for i in range(5):                                                  # ask 5 times for input
        i=int(input("Enter 1~100 to insert in list : "))        # repeat if not input is in 1~100
        while i<1 or i>100:
               print("not in 1~100. Try again")
               i=int(input("Enter 1~100 to insert in list : "))
        linkedList1.insert(i)                                           #insert                    
    linkedList1.printList()                                             #print in array
    for j in range(5):                                                  #ask 5 times for input
        j=int(input("Enter 1~100 to delete in list : "))        #repeat if not valid
        while j<1 or j>100:
            print("not in 1~100. Try Again.")
            j=int(input("Enter 1~100 to delete in list : "))
        linkedList1.delete(j)                                           #delete
    linkedList1.printList()                                             #print in array

    
