#2014311710 Kim Minwoo


#1

list1=[]
while True:
    a=input()
    if a=="q":
        break
    elif int(a)>100:
        a="over"
    list1.append(a)
    

for i in range(len(list1)):
    print(list1[i])


#2

M= int(input("Enter value of M: "))
N= int(input("Enter value of N: "))
commons=[]

if (M==0) or (N==0):
    print("error")
    quit()
elif M>N:
    big=M
else:
    big=N

    
for i in range(1,big+1):
    if M%i==0 and N%i==0:
       commons.append(i)
       
print(max(commons))


#3
phrase= input("Enter a phrase: ").lower()
vowels=['a','e','i','o','u']

num_count=0

for letter in phrase:
    if letter in vowels:
        num_count+=1

print("The phrase contains %d vowels" %(num_count))





#4
sample=input("Enter: ")
sample=sample.upper()

def only_letters(word):
    result_word=""
    ASCII = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in word:
        if letter in ASCII:
            result_word = result_word+letter
    return result_word

def palindrome(sample):

    sample=list(only_letters(sample))
	
    if sample==sample[::-1]:
        return True
    

    return False


if palindrome(sample):
    print(sample, "is a palindrome.")
else:
    print(sample, "is not a palindrome.")
