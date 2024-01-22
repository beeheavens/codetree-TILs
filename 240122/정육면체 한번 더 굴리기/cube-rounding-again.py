#3:30~
def roll_dice(current, direction):
    if(current == 1):
        if(direction == 0):
            return 4
        if(direction == 1):
            return 2
        if(direction == 2):
            return 3
        if(direction == 3):
            return 5
    if(current == 2):
        if(direction == 0):
            return 1
        if(direction == 1):
            return 4
        if(direction == 2):
            return 6
        if(direction == 3):
            return 3
    if(current == 3):
        if(direction == 0):
            return 1
        if(direction == 1):
            return 2
        if(direction == 2):
            return 6
        if(direction == 3):
            return 5
    if(current == 4):
        if(direction == 0):
            return 1
        if(direction == 1):
            return 5
        if(direction == 2):
            return 6
        if(direction == 3):
            return 2
    if(current == 5):
        if(direction == 0):
            return 3
        if(direction == 1):
            return 6
        if(direction == 2):
            return 4
        if(direction == 3):
            return 1
    if(current == 6):
        if(direction == 0):
            return 3
        if(direction == 1):
            return 2
        if(direction == 2):
            return 4
        if(direction == 3):
            return 5


def dfs(start_y,start_x,num):
    stack = []
    start = [start_y,start_x]
    stack.append(start)
    score = num
    check_map = [[0 for i in range(map_size)] for j in range(map_size)]
    check_map[start_y][start_x] = -1
    cur_x = 0
    cur_y = 0
    while(len(stack)!=0):
        cur_x = stack[len(stack)-1][1]
        cur_y = stack[len(stack)-1][0]
        del stack[len(stack)-1]
        for i in range(4):
            if(0<=cur_x+dx[i]<map_size and 0<=cur_y+dy[i]<map_size):
                if(main_map[cur_y+dy[i]][cur_x+dx[i]] == num and check_map[cur_y+dy[i]][cur_x+dx[i]] == 0):
                    check_map[cur_y+dy[i]][cur_x+dx[i]] = -1
                    temp = [cur_y+dy[i],cur_x+dx[i]]
                    stack.append(temp)
                    score += num
    return score

                    
        
####****main****####

map_size, total_round = map(int,input().split())

main_map = []
for i in range(map_size):
    temp_arr = list(map(int,input().split()))
    main_map.append(temp_arr)
dice = 6
dx = [1,0,-1,0] # direction : e s w n
dy = [0,1,0,-1]
direction = 0
position_y = 0
position_x = 0
ans = 0
for i in range(total_round):
    if(position_x+dx[direction] < 0):
        direction = 0
    if(position_x+dx[direction]>= map_size):
        direction = 2
    if(position_y+dy[direction] < 0):
        direction = 1
    if(position_y+dy[direction] >= map_size):
        direction = 3
    position_x += dx[direction]
    position_y += dy[direction]
    ans += dfs(position_y,position_x,main_map[position_y][position_x])
    dice = roll_dice(dice,direction)
    if(dice > main_map[position_y][position_x]):
        direction = (direction+1)%4
    if(dice < main_map[position_y][position_x]):
        direction = direction - 1
        if(direction < 0):
            direction = 3
print(ans)