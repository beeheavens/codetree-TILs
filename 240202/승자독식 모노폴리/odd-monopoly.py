def move():
    global player_num
    """for i in player_map:
        print(i)
    print("-----")
    print(player_data)
    print("---")
    for i in contract_map:
        print(i)"""
    for idx, player in enumerate(player_data): #player data에서 이동 처리
        y = player[0]
        x = player[1]
        move = 0 #이동 여부 판단 flag
        #1. 미계약 땅 확인 
        if(y == -100):
            continue
        for i in range(4): 
            next_y = y+dy[dir_data[idx][player[2]-1][i]-1]#아 데이터에 플레이어 번호를 넣는게 편할거같다.. 안넣으니까 자꾸 index를 찾게돼 -> enumerate를 쓰면 된다!!!
            next_x = x+dx[dir_data[idx][player[2]-1][i]-1]
            if(0<=next_y<map_size and 0<=next_x<map_size):
                if(contract_map[next_y][next_x][0]==0): #미계약 땅
                    player[0] = next_y
                    player[1] = next_x
                    player[2] = dir_data[idx][player[2]-1][i]
                    move = 1
                    break
                    #계약을 지금 하는게 아님
        if(move == 1): #움직였는지 확인을 해야함    
            continue #움직였으면 다음 사람 차례
        for i in range(4): #안움직인 경우, 본인 땅으로 가야함
            next_y = y+dy[dir_data[idx][player[2]-1][i]-1]#아 데이터에 플레이어 번호를 넣는게 편할거같다.. 안넣으니까 자꾸 index를 찾게돼 -> enumerate를 쓰면 된다!!!
            next_x = x+dx[dir_data[idx][player[2]-1][i]-1]
            if(0<=next_y<map_size and 0<=next_x<map_size):
                if(contract_map[next_y][next_x][0]==idx+1): #본인 땅
                    player[0] = next_y
                    player[1] = next_x
                    player[2] = dir_data[idx][player[2]-1][i]
                    move = 1
                    break
    #이제 player map에서 사람을 움직여야 함.

    for i in range(map_size):
        for j in range(map_size):
            player_map[i][j] = 0 #일단 맵을 전부 0으로 초기화
    del_list = []
    for idx, data in enumerate(player_data):
        i = data[0]
        j = data[1]
        if(i == -100):
            continue
        if(player_map[i][j]==0):
            player_map[i][j] = idx+1 #이동 !!!!이럴수가. idx로 넣으니까, 빈칸을 의미하는 0과 플레이어 1번의 idx인 0이 구분이 안된다;
        elif(player_map[i][j]!= 0): #누가 있는 경우
            
            data[0] = -100
            player_num -= 1
            #del_list.append(idx) #없어져야 하는 플레이어 번호 추가
    
    #for i in player_map:
    #    print(i)
    #print("-----")
    #print(player_data)
    #print("---")
    """ 삭제가 완전히 틀렸네..
    for i in range(len(del_list)): #플레이어를 데이터에서 삭제
        del player_data[del_list[i]-i] """

def turn():
    for i in range(map_size):
        for j in range(map_size):
            if(contract_map[i][j][0] != 0):
                contract_map[i][j][1] -= 1
                if(contract_map[i][j][1] == 0):
                    contract_map[i][j][0] = 0

def contract():
    for idx, data in enumerate(player_data):
        if(data[0]==-100):
            continue
        contract_map[data[0]][data[1]][0] = idx+1
        contract_map[data[0]][data[1]][1] = turn_num

def check():
    global player_num
    if (player_num==1):
        return False
    elif(player_num>1):
        return True

####initialize####
global player_num
map_size, player_num, turn_num = map(int,input().split())
player_map = []
contract_map = []
dir_data = []
player_data = []

dx = [0,0,-1,1] # N S W E
dy = [-1,1,0,0] # N S W E

for i in range(map_size): # player map 생성
    temp = list(map(int,input().split()))
    player_map.append(temp)

player_data = list(map(list,input().split())) #player data 생성
for data in player_data:
    data[0] = int(data[0])
for i in range(map_size):
    for j in range(map_size):
        if(player_map[i][j]!= 0):
            player_data[player_map[i][j]-1].insert(0,j)
            player_data[player_map[i][j]-1].insert(0,i)
            


for i in range(player_num): #dir_data 생성
    temp = []
    for j in range(4):
        temp2 = list(map(int,input().split()))
        temp.append(temp2)
    dir_data.append(temp)

contract_map = [[[0,0]for i in range(map_size)]for j in range(map_size)] #contract map 생성

for data in range(len(player_data)): #이거 좀 불편한데, len 안 쓰고 index를 얻는 방법이 없을까? --> enumerate를 쓰면 된다!!
    y = player_data[data][0]
    x = player_data[data][1]
    contract_map[y][x][0] = data+1
    contract_map[y][x][1] = turn_num # contract_map init


####main loop#####
ans = 0
while(check()):
    move()
    turn()
    contract()
    ans+=1
    if(ans>1000):
        ans = -1
        break
    
print(ans)