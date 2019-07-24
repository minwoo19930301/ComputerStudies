string_1=input("Enter the first word:  ").upper()
string_2=input("Enter the second word: ").upper()

def only_letters(word):
    result_word=""
    ASCII = "abcdefghijklmnopqrstuvwxyz"
    for letter in word:
        if letter in ASCII:
            result_word = result_word+letter
    return result_word


string_1=only_letters(string_1)
string_2=only_letters(string_2)

def anagram(w1,w2):

   w1=list(w1).sort()
   w2=list(w2).sort()

   if w1==w2:
        return True
   return False


if anagram(string_1,string_2):
    print("Are anagrams")
else:
    print("Are not anagrams")
