sample=input("Enter: ")
sample=sample.lower()

def only_letters(word):
    result_word=""
    ASCII = "abcdefghijklmnopqrstuvwxyz"
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
