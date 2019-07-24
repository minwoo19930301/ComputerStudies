#2014311710 Kim Minwoo

#1

n = int(input("type the number of the month : "))
if 3<=n<6:
	print("spring")
elif 6<=n<9:
	print("summer")
elif 9<=n<12:
	print("fall")
else:
	print("winter")

#2

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))

if a<b:
	if b<c:
		print("You entered %d %d %d" %(a,b,c))
	elif b>c:
		if a<c:
			print("You entered %d %d %d" %(a,c,b))
		elif a>c:
			print("You entered %d %d %d" %(c,a,b))
elif a>b:
	if b<c:
		if a<c:
			print("You entered %d %d %d" %(b,a,c))
		elif a>c:
			print("You entered %d %d %d" %(b,c,a))
	elif b>c:
		print("You entered %d %d %d" %(c,b,a))
		
#3	
	
gpa = eval(input("Enter your gpa: "))

if 3.6<=gpa:
	if gpa>=3.9:
		honors = " summa cum laude."
	else:
		honors = " magna cum laude."
else:
	if gpa >= 3.3:
		honors = " cum laude."
	else:
		honors = "."
		
print("You graduated" + honors)

#4

