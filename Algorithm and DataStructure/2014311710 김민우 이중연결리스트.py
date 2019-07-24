#2014311710 Minwoo Kim

class Node:
    def __init__(self, data):
        self.data=data
        self.before=None
        self.after=None


start=Node(None)
end=Node(None)

start.after=end
end.before=start

def insert(value):
        newNode=Node(value)
        newNode.before=end.before
        newNode.after=end
        end.before.after=newNode
        end.before=newNode

def delete(value):
        delNode=start
        while delNode:
            if delNode.data==value:
                delNode.before.after=delNode.after
                delNode.after.before=delNode.before
                del delNode
                break
            delNode=delNode.after



