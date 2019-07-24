def findIndex(number,array):  #들어갈 자리를 찾기
    for i in range(0,len(array)):
        if number>=array[i]:            
            t=i+1
    return t

def findNumber(number,array): #빼야할 정수의 자리를 찾기
    for i in range(0,len(array)):
        if number==array[i]:
          s=i
    return s


def insertNum(n,l):         # 리스트 분할 후 대상포함하여 병합
    added_list=l[0:findIndex(n,l)]
    added_list.append(n)
    added_list.extend(l[findIndex(n,l):])
    return added_list

def deleteNum(n,l): #리스트 분할 후 대상 제외하여 병합
    deleted_list=l[0:findNumber(n,l)]
    deleted_list.extend(l[findNumber(n,l)+1:])
    return deleted_list

L1=[1,3,7,11,13,15]  

while 1:
                    
    n=int(input("정수를 입력하시오: ") )
    m=input("삽입하려면 i를, 삭제하려면 d를, 나가려면 q를 누르시오 : ")
    m=m.lower()
    if m=="i":
        L1=insertNum(n,L1)
        print(L1)
    elif m=="d":
        L1=deleteNum(n,L1)
        print(L1)
    elif m=="q":
        break
    else:
        print("잘못 입력하셨습니다.") 
