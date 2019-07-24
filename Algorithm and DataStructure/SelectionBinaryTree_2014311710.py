
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
class SelectTree:
    def __init__(self):
        self.size=0
        self.root=Node(None)
        
    def insert(self,value):
        newNode=Node(value)
        if self.size==0:
            self.root=newNode
            self.size+=1
            return
        cur=self.root
        
        
        while(cur!=None):
            if newNode.value<cur.value:
                pre=cur
                cur=cur.left
            else:
                pre=cur
                cur=cur.right

        if pre.left==None:
            if newNode.value<pre.value:
                    pre.left=newNode
        if pre.right==None:
            if newNode.value>pre.value:
                    pre.right=newNode
                            


    def printTreeBFS(self):
        print("--------------------------------------")
        que=[]
        cur=self.root
        que.append(cur)
        while(que!=[]):
            cur=que.pop(0)
            print(cur.value)
            if cur.left!=None and cur.right!=None:
                que.append(cur.left)
                que.append(cur.right)
            elif cur.left!=None:
                que.append(cur.left)
            elif cur.right!=None:
                que.append(cur.right)
            

    def delete(self,value):
        parent=Node(None)
        parent.left=self.root
        parent.right=self.root
        cur=self.root
        while(cur.value!=value):
            
            if cur.value>value:
                parent=cur
                cur=cur.left
            elif cur.value<value:
                parent=cur
                cur=cur.right
        
        if cur.left==None and cur.right==None:
                if cur==self.root:
                    self.root=Node(None)
                    return
                if parent.left==cur:
                    parent.left=None
                elif parent.right==cur:
                    parent.right=None
                return
        if cur.right==None:
                if cur==self.root:
                    self.root=cur.left
                parent.left=cur.left
                return
        if cur.left==None:
                if cur==self.root:
                    self.root=cur.right
                parent.right=cur.right
                return
        if cur.left!=None and cur.right!=None:
                delete=cur
                cur=cur.left
                pre=cur
                while(cur.right!=None):
                    pre=cur
                    cur=cur.right
                if cur.left!=None:
                    pre.right=cur.left
                elif cur.left==None:
                    pre.right=None
                if parent.right==self.root:
                    self.root=cur
                else:
                    parent.right=cur
                cur.left=delete.left
                cur.right=delete.right
                if cur.left==cur:
                    cur.left=None
                if cur.right==cur:
                    cur.right=None
                return  
        


        
t=SelectTree()
t.printTreeBFS()
t.insert(10)
t.insert(3)
t.insert(15)
t.insert(2)
t.insert(1)
t.insert(5)
t.insert(11)
t.insert(17)
t.insert(16)
t.insert(20)
t.printTreeBFS()
t.delete(1)
t.printTreeBFS()
t.delete(10)
t.printTreeBFS()
t.delete(17)
t.printTreeBFS()
t.delete(11)
t.printTreeBFS()
t.delete(5)
t.printTreeBFS()
t.delete(3)
t.printTreeBFS()
t.delete(16)
t.printTreeBFS()
t.delete(20)
t.printTreeBFS()
t.delete(15)
t.printTreeBFS()
