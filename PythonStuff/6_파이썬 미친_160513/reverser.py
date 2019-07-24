word = input("Enter")

def reverser(word):
    
    rword=""
    for i in word:
        rword=i+rword
    return rword


print(reverser(word))
