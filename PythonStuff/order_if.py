num1= int(input("type any number for num1"))
num2= int(input("type any number for num2"))
num3= int(input("type any number for num3"))

if num1 > num2 :
   if num2 > num3 :
      print (num3,num2,num1)
   else :
      if num1 > num3 :
         print (num2,num3,num1)
      else :
         print  (num2,num1,num3)
else :
   if num2 < num3 :
      print (num1,num2,num3)
   else:
      if num1 > num3 :
         print (num3,num1,num2)
      else:
         print (num1,num3,num2)
