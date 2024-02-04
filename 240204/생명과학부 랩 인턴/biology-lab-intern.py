def catch(pos):
    for i in range(n):
        if(main_map[i][pos]!=0):
            idx = main_map[i][pos] - 1
            if(mold_data[idx]==-100):
                continue
            value = mold_data[idx][4]
            mold_data[idx][4] = -100
            main_map[i][pos] = 0
            return value
               
    return 0

def move():
    for idx, data in enumerate(mold_data):
        if(data[4]==-100) : continue
        direction = data[3]
        for i in range(data[2]):
            next_y = data[0] + dy[direction]
            next_x = data[1] + dx[direction]
            if(0<=next_x<m and 0<=next_y<n):
                data[0] = next_y
                data[1] = next_x
            else:
                if(direction == 0): data[3] = 1
                elif(direction == 1): data[3] = 0
                elif(direction == 2): data[3] = 3
                elif(direction == 3): data[3] = 2
                direction = data[3]
                next_y = data[0] + dy[direction]
                next_x = data[1] + dx[direction]
                data[0] = next_y
                data[1] = next_x

def eat():
    for i in range(n):
        for j in range(m):
            main_map[i][j] = 0
    for idx, data in enumerate(mold_data):
        if(data[4]==-100): continue
        y = data[0]
        x = data[1]
        if(main_map[y][x]==0):
            main_map[y][x] = idx+1
        else:
            prev_idx = main_map[y][x]-1
            if(mold_data[prev_idx][4]<data[4]):
                main_map[y][x] = idx+1
                mold_data[prev_idx][4] = -100
    """ret_data = []
    for i in range(n):
        for j in range(m):
            if(main_map[i][j]!=0):
                ret_data.append(mold_data[main_map[i][j]-1])
    return ret_data"""

#### main ####
n,m,mold_num = map(int,input().split())

main_map = [[0 for i in range(m)] for j in range(n)]
mold_data = [] #y,x, 속력, 방향, 크기
dx = [0,0,1,-1] # N S E W
dy = [-1,1,0,0]
for i in range(mold_num):
    temp = list(map(int,input().split()))
    temp[0] -= 1
    temp[1] -= 1
    mold_data.append(temp)

for idx, data in enumerate(mold_data):
    y = data[0]
    x = data[1]
    main_map[y][x] = idx+1

position = 0
ans = 0
#### main loop ####

for i in range(m):
    ans += catch(i)
    move()
    eat()

print(ans)