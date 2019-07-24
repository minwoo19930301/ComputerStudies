
def isbn(number):
    try:
        numberreal = number
        #keeps real number with "-"
        numberzero = number.replace("-", "")
        #this makes sure python doesnt drop the first 0 if it is at the start
        number = number.replace("-", "")
        number = int(number)
        number = str(numberzero)
        print("The ISBN Number Entered is", numberreal)
        num = int(number[0]) * 10 + int(number[1]) * 9 + int(number[2]) * 8 + int(number[3]) * 7 + int(number[4]) * 6 + int(number[5]) * 5 + int(number[6]) * 4 + int(number[7]) * 3 + int(number[8]) * 2
        num = num%11
        checknum = 11 - num

        print("The Check Digit Should Be", checknum, "and the one in the code provided was", number[9])
        if int(checknum) == int(number[9]):
            print("The Check Digit Provided Is Correct")
        else:
            print("The Check Digit Provided Is Incorrect")
    except ValueError:
        print("Not Valid Number")
        error()
    except IndexError:
        print("Not 10 Digits")
        error()



def error():
    print("Error")

running = True
while running == True:
    isbn(input("What is the isbn 10 digit number? "))
    restart = input("Do You Want Restart?")
    restart = restart.lower()
    if restart in ("yes", "y", "ok", "sure", ""):
        print("Restarting\n" + "-" * 34)
    else:
        print("closing Down")
        running = False
