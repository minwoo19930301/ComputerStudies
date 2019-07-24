#-*-coding:utf-8 -*-
#2014311710 김민우
#1
x = input("숫자를 써보세요... \n내가 두 배로 갚아줄테니깐! : ")
x = int(x)*2
print(x)


#2 

x= input("\n\t숫자를 쓰시오 ")
y= input("\n\t한번더.. 그럼 더한 값과 곱한 값을 보여주지 ")
z=int(x)+ int(y)
w=int(x)* int(y)
print(z,w)

#3
s = input("\n이동하는 속도값(km/h)을 써보세요. ")
t = input("\n이동하는 동안 보낸 시간(h)을 쳐보세요. ")
distance = float(s)* float(t)
print ("\n그럼 이 정도를 이동했겠군요. %r km" %(distance))
