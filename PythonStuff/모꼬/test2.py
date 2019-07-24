import math
def lencalculation(x,y):
    t=math.sqrt(pow(x,2)+pow(y,2))
    return t
def assignStudents(tentfile,studentfile):
    ft=open(tentfile,'r')
    tline=ft.read()     
    tline=tline.split('\n')     #줄 바꾸기 기준으로 자르기
    print(tline)
    i=0
    try:
        while 1:
            tline[i]=tline[i].split(',')    # ,를 기준으로 자르기
            i=i+1
    except IndexError:
        ct=i        #i에 저장된 카운트 된 텐트 갯수를 ct에 저장
    print(ct)
    fs=open(studentfile,'r')
    sline=fs.read()
    sline=sline.split('\n')
    i=0
    try:
        while 1:
            sline[i]=sline[i].split(',')
            i=i+1
    except IndexError:
        cs=i    # i에 저장된 카운트 된 학생수를 cs에 저장
    c=int(cs/ct)+1      # c에는 텐트당 들어갈 수 있는 최대 학생수
    i=0
    while i<ct:
        tline[i].append(0)  #tline[i][3]에 텐트에 들어간 학생수를 카운트 하기위해 0으로 초기화
        i=i+1
    i=0
    while i<cs:
        sline[i].append(0)  #sline[i][3]에 텐트 아이디를 저장하기 위해 공간 확보
        i=i+1
    i=0
    while i<cs:
        sline[i].append(0)  #sline[i][4]에 텐트 거리를 저장하기 위해 공간 확보
        i=i+1
    i=0
    stdistance=[[0 for col in range(0)] for row in range(cs)]   #텐트와 학생의 거리를 저장할 리스트 stdistance선언
    while i<cs:
        stdistance[i].append(i+1)   #stdistance에 학생 id부여(즉 stdistance[i][0]은 전부 학생 ID가 저장됨)
        i=i+1
    i=0
    while i<cs:
        j=0
        while j<ct:
            t=lencalculation(float(sline[i][1])-float(tline[j][1]),float(sline[i][2])-float(tline[j][2]))
            stdistance[i].append(t)
            if j==0:
                k=t     #k는 가장 가까운 거리에 있는 텐트까지의 거리
                tcount=j    #tcount는 몇 번째 텐트에 학생이 들어갔는지 카운트
            elif k>t:
                k=t
                tcount=j
            j=j+1
        sline[i][3]=tcount+1   #학생이 들어간 텐트의 id를 sline[i][3]에 저장
        sline[i][4]=k      #학생이 들어간 텐트까지의 거리를 sline[i][4]에 저장
        tline[tcount][3]=tline[tcount][3]+1 #텐트에 들어간 학생의 수 카운트
        t=0
        while t<ct:
            y=0
            while y<cs:     #한 텐트에 학생 전부가 들어갈 경우를 가정해서 학생 수 만큼 루프를 돌림
                if tline[t][3]>int(cs/ct)+1: #만약 tline[t][3]에 있는 학생 수가 학생수/텐트수+1보다 크면
                    j=0
                    jcount=0    # 밑에 if문에서 stminus(텐트와 학생의 거리의 차이)에 처음 값이 주어졌을 때 값을 정하고 다른 값들과 비교하기 위해서 jcount설정
                    while j<cs:     
                        if sline[j][3]==t+1: #sline에 저장된 텐트 ID와 while문 안에서 현재 텐트 아이디가 동일할 경우
                            jcount=jcount+1
                            #바로 밑의 두개의 while문에서 수용량이 넘은 텐트에 들어간 어떤 학생의 다음 번째로 가까운 텐트를 구함
                            p=0
                            while p<ct: 
                                if sline[j][4]<stdistance[j][p+1]: #sline[j][4]에 있는 학생과 텐트의 거리가 stdistance[j][p+1]의 값보다 작을 경우
                                    k=stdistance[j][p+1]-sline[j][4] #처음 sline[j][4]보다 큰 경우 sline[j][4]와 stdistance[j][p+1]의 차이를 k에 저장
                                    t2=p  #t2에 몇 번째 텐트인지 저장(이때 j는 어떤 학생인지를 나타내고 있음)
                                    break
                                p=p+1
                            p=0
                            while p<ct:
                                if sline[j][4]<stdistance[j][p+1]:
                                    r=stdistance[j][p+1]-sline[j][4] #r에 이후 sline[j][4]보다 큰 경우 line[j][4]와 stdistance[j][p+1]의 차이를 r에 저장
                                    if r<k: #r과 k를 비교해서 더 작을 경우
                                        k=r #k에 r을 저장
                                        t2=p #몇 번째 텐트인지 저장
                                p=p+1
                            # 위의 두개의 while문에서 구한 거리를 밑의 if~ while에서 비교해서 수용량을 넘은 텐트에 들어간 학생들 중 다음으로 가까운 텐트와의 거리가 가장 가까운 학생 찾기
                            if jcount==1: #처음 위의 tline[t][3]>int(cs/ct)+1조건을 성립한 경우(즉 처음 if tline[t][3]>int(cs/ct)+1을 만족해 while문을 돌 때)
                                stminus=k #stminus에 두 거리의 차이 값을 대입.
                                t3=t2 #그때 몇 번째 텐트인지 저장
                                tj=j #그때 어떤 학생인지 저장
                            p=0
                            while p<ct:
                                if stminus>k: #stminus값 중 최소값 찾기
                                    stminus=k
                                    t3=t2 #그때 몇 번째 텐트인지 저장
                                    tj=j #그때 어떤 학생인지 저장
                                p=p+1
                        j=j+1
                    sline[tj][4]=stdistance[tj][t3+1] #sline[tj][4]에 저장된 거리 값을 다음 번째로 가까운 텐트의 거리 값으로 수정
                    sline[tj][3]=t3+1 #sline[tj][3]에 저장된 텐트 ID를 다음 번째로 가까운 거리의 텐트 ID로 변경
                    tline[t][3]=tline[t][3]-1 #학생수/텐트수+1보다 컸던 tline[t][3]의 학생수 값에서 1을 뺌
                    tline[t3][3]=tline[t3][3]+1 #다음 번째로 가까운 거리의 텐트에 학생수 값에 1을 더해줌
                    if tline[t3][3]>int(cs/ct)+1: #만약 새로 증가시킨 텐트의 학생수가 다시 학생수/텐트수+1보다 클 경우
                        t=t3 #t 값을 새로 증가시킨 텐트의 값으로 변화시켜 위의 루프를 다시 돌림.
                y=y+1
            t=t+1
        i=i+1
    f=open("output.csv",'w')
    i=0
    while i<cs:
        stid=sline[i][0]
        tid=str(sline[i][3])
        stdis=str(sline[i][4])
        f.write(stid)
        f.write(',')
        f.write(tid)
        f.write(',')
        f.write(stdis)
        f.write('\n')
        i=i+1
assignStudents("tents.csv","students.csv")

