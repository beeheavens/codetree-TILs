'''도우 말기 함수를 roll_dough라고 했는데, 말린 도우를 rolled_dough라고 했다.
    이러면 알아보기 좀 헷갈린데 어떻게 이름을 지어야 할까?'''

'''보통 메인에 만들어 둔 list가 전역으로 사용 가능한데, 왜 이번엔 global을 붙여야 작동하지?
    파이썬의 전역 변수 기준이 좀 모호한데?'''


def add_flour():
    #이때 dough는 한 줄이다
    min = dough[0][0]
    for i in dough[0]:
        if(i < min):
            min = i
    for idx, value in enumerate(dough[0]):
        if(value==min):
            dough[0][idx]+= 1

def roll_dough():
    global dough
    len_upper_dough = 0
    rolled_dough = []
    if(len(dough)>1): # 한줄이 아닌 경우
        len_upper_dough = len(dough[0])
    #말기 가능한지 체크
    if(len(dough) > len(dough[len(dough)-1]) - len(dough) + 1):
        return -1
    #도우가 한줄인 경우
    if(len_upper_dough==0):
        dough = [[dough[0][0]],dough[0][1:]]
        return 1
    #한줄이 아닌 경우
    elif(len_upper_dough>0):
        for i in range(len_upper_dough):
            temp = []
            for j in dough:
                temp.insert(0,j[i])
            rolled_dough.append(temp)
        rolled_dough.append(dough[len(dough)-1][len_upper_dough:])
        dough = rolled_dough
        return 1
    
def push_dough():
    #똑같은 모양의 배열 생성
    adder_dough = []
    dx = [1,0]
    dy = [0,1]
    for i in dough:
        temp = [0 for j in range(len(i))]
        adder_dough.append(temp)
    for idx_y, value in enumerate(dough):
        for idx_x, value2 in enumerate(value):
            for i in range(2):
                next_x = idx_x + dx[i]
                next_y = idx_y + dy[i]
                try:
                    d = (max(value2,dough[next_y][next_x]) - min(value2,dough[next_y][next_x])) // 5
                    
                    if(value2 >= dough[next_y][next_x]):
                        adder_dough[idx_y][idx_x] -= d
                        adder_dough[next_y][next_x] += d
                    elif(value2 < dough[next_y][next_x]):
                        adder_dough[idx_y][idx_x] += d
                        adder_dough[next_y][next_x] -= d
                except:
                    pass
    for i in range(len(dough)):
        for j in range(len(dough[i])):
            dough[i][j] += adder_dough[i][j]
    
def flatten():
    temp = []
    global dough
    for i in range(len(dough[len(dough)-1])):
        for j in range(len(dough)-1,-1,-1):
            try:
                temp.append(dough[j][i])
            except:
                pass
    dough = temp

def fold():
    #한번 접기
    global dough
    part_1 = dough[:((len(dough))//2)]
    part_2 = dough[len(dough)//2:]
    part_1.reverse()
    one_foled_dough = []
    one_foled_dough.append(part_1)
    one_foled_dough.append(part_2)
    #두번 접기
    temp = []
    for i in one_foled_dough:
        part_1 = i[:((len(i))//2)]
        part_2 = i[(len(i))//2:]
        part_1.reverse()
        temp.insert(0,part_1)
        temp.append(part_2)
    dough = temp

def check():
    return (max(dough[0]))-(min(dough[0]))


### main ###
flour_list, maxMinDiff = map(int,input().split())
global dough
dough = [list(map(int,input().split()))]

ans = 0
while(1):
    if(check()<=maxMinDiff):
        break
    add_flour()
    result = 1
    while(result==1):
        result = roll_dough()
    push_dough()
    flatten()
    fold()
    push_dough()
    flatten()
    dough = [dough]
    ans+=1
print(ans)