#4:15~
def collect(sy_pos):
    y = -1
    for i in range(n):
        if(main_map[i][sy_pos] != 0):
            y = i
            break
    size = 0
    if(y != -1):   #잡은 경우
        size = mold_data[main_map[y][sy_pos]-1][4]
        del mold_data[main_map[y][sy_pos]-1]
        for i in range(n):
            for j in range(m):
                main_map[i][j] = 0
        for idx, value in enumerate(mold_data):
            y = value[0]
            x = value[1]
            main_map[y][x] = idx+1
    return size

def move():
    for mold in mold_data:
        distance = mold[2]
        direction = mold[3]
        for i in range(distance):
            y = mold[0]
            x = mold[1]
            next_y = y + dy[direction]
            next_x = x + dx[direction]
            if(next_y<0 or next_y >= n):
                if(direction == 0): direction = 1
                elif(direction == 1): direction = 0
                next_y = y + dy[direction]
            if(next_x<0 or next_x >= m):
                if(direction == 2): direction = 3
                elif(direction == 3): direction = 2
                next_x = x + dx[direction]
            mold[0] = next_y
            mold[1] = next_x
            mold[3] = direction
    
def eat():
    eaten_list = []
    for i in range(n):
        for j in range(m):
            main_map[i][j] = 0
    for idx,i in enumerate(mold_data):
        if(main_map[i[0]][i[1]] == 0): main_map[i[0]][i[1]] = idx+1
        elif(main_map[i[0]][i[1]]!=0): #겹치는 경우
            local_mold = mold_data[main_map[i[0]][i[1]]-1][4] #기존 곰팡이 크기
            if(local_mold>i[4]): #기존 곰팡이가 큰 경우
                eaten_list.append(idx)
            elif(local_mold<i[4]): #새 곰팡이가 큰 경우
                eaten_list.append(main_map[i[0]][i[1]]-1)
                main_map[i[0]][i[1]] = idx+1
    eaten_list.sort(reverse=True)
    for i in eaten_list:
        del mold_data[i]
    for i in range(n):
        for j in range(m):
            main_map[i][j] = 0
    for idx,i in enumerate(mold_data):
        main_map[i[0]][i[1]] = idx+1




### Main ###
n,m,mold_num = map(int,input().split())
mold_data = []
for i in range(mold_num):
    temp = list(map(int,input().split())) # y,x, 거리, direction,크기
    temp[0] -= 1
    temp[1] -= 1
    temp[3] -= 1
    mold_data.append(temp)

dx = [0,0,1,-1] # 북 남 동 서
dy = [-1,1,0,0]
main_map = [[0 for i in range(m)]for j in range(n)]

for idx,i in enumerate(mold_data):
    y = i[0]
    x = i[1]
    main_map[y][x] = idx+1

ans = 0
for i in range(m):
    ans += collect(i)
    move()
    eat()
print(ans)