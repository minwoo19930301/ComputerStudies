class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class Deque:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def isEmpty(self):
        if self.head.next==self.tail:
            return True
        return False

    def enqHead(self, value):
        newNode=Node(value)
        if self.isEmpty():
            self.head.next=newNode
            self.tail.prev=newNode
            newNode.prev=self.head
            newNode.next=self.tail
            return
        self.head.next.prev=newNode
        newNode.next=self.head.next
        self.head.next=newNode
        newNode.prev=self.head

    def enqTail(self, value):
        newNode=Node(value)
        if self.isEmpty():
            self.head.next=newNode
            self.tail.prev=newNode
            newNode.prev=self.head
            newNode.next=self.tail
            return
        self.tail.prev.next=newNode
        newNode.prev=self.tail.prev
        self.tail.prev=newNode
        newNode.next=self.tail
        
        
    def deqHead(self):
        if self.isEmpty():
            print("Already Empty")
            return
        self.head.next=self.head.next.next
        self.head.next.prev=self.head


    def deqTail(self):
         if self.isEmpty():
             print("Already Empty")
             return
         self.tail.prev=self.tail.prev.prev
         self.tail.prev.next=self.tail
    
    def printDeq(self):
        arr=[]
        cur=self.head
        while(cur.next!=self.tail):
            cur=cur.next
            arr.append(cur.data)
        print(arr)
        
d=Deque()

'''
class Deque:
    def __init__(self):
        self.deq=[]
        
    def isEmpty(self):
        if self.deq==[]:
            return True
        return False

    def enqHead(self, value):
        if self.isEmpty():
            self.deq.append(value)
            return
        self.deq=[value]+self.deq

    def enqTail(self, value):
        if self.isEmpty():
            self.deq.append(value)
            return
        self.deq=self.deq+[value]

    def deqHead(self):
        if self.isEmpty():
            print("Already Empty")
            return
        del self.deq[0]

    def deqTail(self):
        if self.isEmpty():
            print("Already Empty")
            return
        del self.deq[-1]

        

'''
