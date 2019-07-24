#2014311710 Kim Minwoo (김민우)


#1

def getContinue():
    while 1:
        ans=input("Do you want to continue (y/n)").lower()
        if ans=="y" or ans=="n":
            break    
    if ans=="y":
        val=True
    if ans=="n":
        val=False
    return val



print(getContinue())

#2

def convertCases(string):
    string=list(string)
    a=[]
    for word in string:
        if word.isupper():
            word=word.lower()
            a.append(word)
        elif word.islower():
            word=word.upper()
            a.append(word)

    return("".join(a))

    


word=input("word: ")
print(convertCases(word))


#3

def printStars(d):
    while d:
        print(min(d),": ",end='')
        print("*"*d[min(d)])
        del d[min(d)]
    
        



dic={"A":8,"D":3, "B":15, "F":2, "C":6}
printStars(dic)


#4

def makeEvenFirst(list1):
    
    even=[]
    odd=[]
    for num in list1:
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
        
    new_list=even+odd

    return new_list

listA=[1,4,14,2,1,3,5,6,23]
print(makeEvenFirst(listA))


#5


def getSpamLines(filename):
    infile=open(filename,'r')
    lines=[line.rstrip() for line in infile]
    infile.close()
    count=0
    for line in lines:
        if line.startswith("SPAM-Confidence:") and eval(line[16:])>0.8:
            count+=1
        else:
            pass

    return count

file1="spam.txt"
print(getSpamLines(file1))


#6
from random import *
def generateSentence(listA,listB):
    
    return (choice(listA) +" "+ choice(listB))

A= ['I','You','He','We','She']
B= ['ran','smiled','slept']

print(generateSentence(A,B))

    
