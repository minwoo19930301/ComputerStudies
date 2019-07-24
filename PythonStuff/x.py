#1
n = float(input("Type the number of seconds \n between lightning and thunder. : "))
d = n/5
print("The distance from storm is " +str(d) + "miles.")
#2
m = int(input("type the amount of months : "))
y = m//12
m_2 = m%12
print (str(m) +"months equals "+ str(y) + "years and " + str(m_2) + "months.")

#3
salary = float(input("Enter the beginning salary: $"))
new_salary = float((salary*1.1)*0.9)
change = round(float(((new_salary-salary)/salary)*100),2)

print("New salary: $" + str(new_salary) + "\nChange:" + str(change) + "%")

#4
s = input("Enter any sentence. \n\n\t")