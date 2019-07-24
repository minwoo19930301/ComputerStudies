#2014311710 Kim Minwoo
#1
team = input("Enter name of the team: ")
win = int(input("Enter numbers of games won: "))5
lose = int(input("Enter numbers of games lost: "))
if win ==0 and lose==0:
	win_rate=0
else:	
	win_rate = round((win/(win+lose)*100),1)

print("%s won %r" %(team, win_rate), end="")
print("% of their games." )

#2
p = eval(input("\nEnter principal: "))
r = float(input("Enter interest rate (as %): "))
n = eval(input("Enter number of years: "))
future_value= p*((1+(r/100))**n)
print("Future value: $",'{0:,.2f}'.format(future_value))

#3
num = float(input("\nEnter number of copies: "))
if num>100:
	cost = (100*0.05) + (num-100)*0.03
else:
	cost = num*0.05
print("Cost is : $"'{0:,.2f}'.format(cost))

#4
w = eval(input("\nEnter hourly wage: $"))
h = eval(input("Enter number of hours worked: "))
if h>=40:
	g=(40*w) + 1.5*w*(h-40)
else:
	g=(w*h)
	
print("Gross pay for week is : $",'{0:,.2f}'.format(g),".")

#5
a = int(input("\nEnter first score: "))
b = int(input("Enter second score: "))
c = int(input("Enter third score: "))

if a<b:
	if b<c:
		s = a, b, c
	elif b==c:
		s = a, b, c
	else:
		if a< c:
			s = a, b, c
		elif a==c:
			s = a, b, c
		else:
			s = c, a, b
			
elif a>b:
	if b<c:
		if c<a:
			s = b, c, a
		elif c==a:
			s = b, a, c
		else:
			s = b, a, c
	elif b==c:
		s = b, c, a
	else:
		s = c, b, a
elif a==b:
	if b<c:
		s = a, b, c
	elif b==c:
		s= a, b, c
	else:
		s= c, a, b

average= (s[1] + s[2])/2
print("Average of two highest\nscores is "+str(average))
input("S")
