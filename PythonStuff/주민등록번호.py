kssn = (input("주민등록번호 : "))

logic = [2,3,4,5,6,7,8,9,2,3,4,5]

number = 0

for i in range(0, len(logic)):

    number += int(kssn[i]) * int(logic[i])

if 11-(number%11) == int(kssn[12]):

    print ("이 주민등록번호는 유효한 주민등록번호 입니다.")

else:

    print ("이 주민등록번호는 유효하지 않은 주민등록번호 입니다." )
