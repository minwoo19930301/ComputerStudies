def countLetters(string):
    string=string.strip().replace(' ','')
    list1=[]
    for word in string:
        list1.append(word)
        if word.isdigit():
            list1.remove(word)
    newDict={}
    for word in list1:
        newDict[word]=list1.count(word)


    return newDict


    

string=input("Example: ").lower()    
print(countLetters(string))
