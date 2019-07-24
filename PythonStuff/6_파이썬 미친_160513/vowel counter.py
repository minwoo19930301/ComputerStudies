phrase= input("Enter a phrase: ").lower()
vowels=['a','e','i','o','u']
num_count=0

for letter in phrase:
    if letter in vowels:
        num_count+=1

print("The phrase contains %d vowels" %(num_count))

