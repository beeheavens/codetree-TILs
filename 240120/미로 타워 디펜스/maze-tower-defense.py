def attack(direction, attack_range): # 몬스터 공격 , e s w n 
    global ans
    for i in range(attack_range):
        ans += main_map[center_coor+dy[direction]*(i+1)][center_coor+dx[direction]*(i+1)]
        main_map[center_coor+dy[direction]*(i+1)][center_coor+dx[direction]*(i+1)] = 0
    
def lower_dim(): # 2차원 배열을 1차원화
    low_dim_arr = []
    cur_x = 0
    cur_y = 0
    direction = 0
    temp_map = [[0 for i in range(map_size)] for j in range(map_size)]
    while(cur_x != center_coor or cur_y != center_coor):
        low_dim_arr.append(main_map[cur_y][cur_x])
        temp_map[cur_y][cur_x] = 1
        # 다음 움직임이 map을 벗어나는지 확인
        if(cur_x+dx[direction]<0 or cur_x+dx[direction]>= map_size or cur_y+dy[direction]<0 or cur_y+dy[direction]>= map_size):
            direction = (direction+1) % 4 # direction 바꿔주기
        # 다음 움직임이 이미 지나간 곳인지 확인
        if(temp_map[cur_y+dy[direction]][cur_x+dx[direction]] == 1): 
            direction = (direction+1) %4 # direction 바꿔주기
        cur_x = cur_x+dx[direction]
        cur_y = cur_y+dy[direction]
    return low_dim_arr

def empty_deletion(one_dim_arr):
    for i in range(len(one_dim_arr)):
        if(one_dim_arr[i] != 0):
            start = i
            break
    for j in range(start,len(one_dim_arr)):
        if(one_dim_arr[j] == 0):
            del one_dim_arr[j]
            one_dim_arr.insert(0,0) # ***** insert를 안해주면 리스트 원소 수가 바뀌어서 index range 오류가 발생함!!!
    
def four_deletion(one_dim_arr): #4번 이상 중복 삭제
    global ans
    one_dim_arr.append(-1)
    while(1):
        last = 0
        cont = 0
        start = 0
        flag = 0
        for i in range(len(one_dim_arr)):
            if(one_dim_arr[i] != last):
                if(last != 0 and cont > 4):
                    ans += last * (cont-1)
                    one_dim_arr = one_dim_arr[0:start] + one_dim_arr[i:len(one_dim_arr)]
                    flag = 1
                    break
                start = i
                cont = 1
                last = one_dim_arr[i]
            if(one_dim_arr[i] == last):
                cont += 1
        if(flag == 0):
            break
    del one_dim_arr[len(one_dim_arr)-1]
    return one_dim_arr

def make_monster(one_dim_arr):
    temp_arr = []
    last = one_dim_arr[0]
    cont = 0
    for i in one_dim_arr:
        if(i == 0):
            temp_arr.append(cont)
            temp_arr.append(last)
            break
        if(i != last):
            temp_arr.append(cont)
            temp_arr.append(last)
            cont = 1
            last = i
            continue
        if(i == last):
            cont += 1
    return temp_arr
        
def upper_dim(one_dim_arr):
    cur_x = 0
    cur_y = 0
    direction = 0
    index = 0
    temp_map = [[0 for i in range(map_size)] for j in range(map_size)]
    while(cur_x != center_coor or cur_y != center_coor):
        main_map[cur_y][cur_x] = one_dim_arr[index]
        temp_map[cur_y][cur_x] = 1
        # 다음 움직임이 map을 벗어나는지 확인
        if(cur_x+dx[direction]<0 or cur_x+dx[direction]>= map_size or cur_y+dy[direction]<0 or cur_y+dy[direction]>= map_size):
            direction = (direction+1) % 4 # direction 바꿔주기
        # 다음 움직임이 이미 지나간 곳인지 확인
        if(temp_map[cur_y+dy[direction]][cur_x+dx[direction]] == 1): 
            direction = (direction+1) %4 # direction 바꿔주기
        cur_x = cur_x+dx[direction]
        cur_y = cur_y+dy[direction]
        index += 1

##****** main *****##
map_size, total_round = map(int,input().split())
center_coor = map_size // 2 # 미로의 중심 좌표
global ans
ans = 0
dx = [1,0,-1,0] # eswn
dy = [0,1,0,-1] # eswn

main_map = []
for i in range(map_size): # 미로 생성
    temp_map = list(map(int,input().split()))
    main_map.append(temp_map)

attack_data = [] # 공격
for i in range(total_round):
    temp_attack = list(map(int,input().split()))
    attack_data.append(temp_attack)

# 준비완료
for l in range(total_round):
    attack(attack_data[l][0],attack_data[l][1])
    low_dim = lower_dim()
    empty_deletion(low_dim)
    low_dim = four_deletion(low_dim)
    returned_arr = make_monster(list(reversed(low_dim)))
    while(len(returned_arr) < map_size*map_size - 1):
        returned_arr.append(0)
    if(len(returned_arr)>=map_size*map_size):
        returned_arr = returned_arr[0:map_size*map_size]
    returned_arr = list(reversed(returned_arr))
    upper_dim(returned_arr)



print(ans)