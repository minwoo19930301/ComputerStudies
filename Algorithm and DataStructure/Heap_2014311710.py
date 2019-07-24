class Heap:
        #initiated instance variables
        #just to easily make indexes easier starting from 1 
         lis=[None]
         noOfList=0

         def isEmpty(self):
                  if self.noOfList==0:
                           return True
                  else:
                           return False

         def insertHeap(self, heap):
                  self.noOfList+=1
                  #first just add in end
                  self.lis.append(heap)
                  #the index of that will be the end, which also equals to the size
                  idx=self.noOfList
                  while 1:
                          #if first idx it is the root
                           if idx==1: 
                                    break
                        #if parent is larger than child then it is fine
                           if self.lis[idx]<self.lis[idx//2]:
                                    break
                        #unless former cases, swap upwards and track index
                           else:
                                    self.lis[idx],self.lis[idx//2]=self.lis[idx//2],self.lis[idx]
                                    idx=idx//2
                    #if done with loop show the heap
                  self.printHeap()
                           
                           
         def deleteHeap(self):
                #in case of error : deleting nothing
                  if (self.isEmpty()):
                           print("already empty")
                           return
                  self.noOfList-=1
                  #because of dynamic array structure of python
                  #change last and root first and then remove
                  self.lis[-1],self.lis[1]=self.lis[1],self.lis[-1]
                  del(self.lis[-1])
                  idx=1
                  #starting from the root swap with larger child if necessary
                  #find the larger child first
                  while 1:
                           left=2*idx
                           right=2*idx+1
                           #in case there are 2 childs
                           if right<=self.noOfList:
                                    if self.lis[left]>self.lis[right]:
                                             larger=left
                                    else:
                                             larger=right
                            #in case there is only left child
                           if left<=self.noOfList:
                                    larger=left
                            #no childs
                           else:
                                    break
                            #swap and change our focus to larger child as what we did on our root
                            #loop will continue until leaf node
                           self.lis[idx],self.lis[larger]=self.lis[larger],self.lis[idx]
                           idx=larger
                  #print heap if done with the loop
                  self.printHeap()
                           


         def printHeap(self):
                 #the heap does not count index 0 :None
                  print(self.lis[1:])
                  
#Main
import random
#make object
h=Heap()
#insert and delete 10 times with random numbers
for i in range(10):
    r=random.randint(1,100)
    print("insert ",r)
    h.insertHeap(r)
for j in range(10):
    print("delete")
    h.deleteHeap()
# just another to check deleting errors with empty heaps
h.deleteHeap()
