def move():
    for idx,unit in enumerate(unit_data):
        y = unit[0]
        x = unit[1]
        direction = unit[2]
        next_y = y + dy[direction]
        next_x = x + dx[direction]
        if(0<=next_y<map_size and 0<= next_x<map_size): #밖으로 나가지 않음
            cur_position = unit_map[y][x]
            units = cur_position[cur_position.index(idx+1):]
            if(color_map[next_y][next_x] == 0): #흰색 판
                for i in units:
                    unit_map[next_y][next_x].append(i)
                    unit_data[i-1][0] = next_y
                    unit_data[i-1][1] = next_x
                unit_map[y][x] = unit_map[y][x][:cur_position.index(idx+1)]
            elif(color_map[next_y][next_x] == 1) : #빨간색 판
                units.reverse()
                for i in units:
                    unit_map[next_y][next_x].append(i)
                    unit_data[i-1][0] = next_y
                    unit_data[i-1][1] = next_x
                unit_map[y][x] = unit_map[y][x][:cur_position.index(idx+1)]
            elif(color_map[next_y][next_x]==2 or next_y < 0 or next_y>=map_size or next_x<0 or next_x >= map_size) : #파란색 판
                if(direction == 0):
                    direction = 1
                elif(direction == 1):
                    direction = 0
                elif(direction == 2):
                    direction = 3
                elif(direction == 3):
                    direction = 2
                next_y = y + dy[direction]
                next_x = x + dx[direction]
                if(color_map[next_y][next_x] == 0): #흰색 판
                    for i in units:
                        unit_map[next_y][next_x].append(i)
                        unit_data[i-1][0] = next_y
                        unit_data[i-1][1] = next_x
                    unit_map[y][x] = unit_map[y][x][:cur_position.index(idx+1)]
                elif(color_map[next_y][next_x] == 1) : #빨간색 판
                    units.reverse()
                    for i in units:
                        unit_map[next_y][next_x].append(i)
                        unit_data[i-1][0] = next_y
                        unit_data[i-1][1] = next_x
                    unit_map[y][x] = unit_map[y][x][:cur_position.index(idx+1)]
                elif(color_map[next_y][next_x]==2 or next_y < 0 or next_y>=map_size or next_x<0 or next_x >= map_size):
                    pass
                unit_data[idx][2] = direction
        elif(next_y < 0 or next_y>=map_size or next_x<0 or next_x >= map_size): #튀어나감
            cur_position = unit_map[y][x]
            units = cur_position[cur_position.index(idx+1):]
            if(direction == 0):
                direction = 1
            elif(direction == 1):
                direction = 0
            elif(direction == 2):
                direction = 3
            elif(direction == 3):
                direction = 2
            next_y = y + dy[direction]
            next_x = x + dx[direction]
            if(color_map[next_y][next_x] == 0): #흰색 판
                for i in units:
                    unit_map[next_y][next_x].append(i)
                    unit_data[i-1][0] = next_y
                    unit_data[i-1][1] = next_x
                unit_map[y][x] = unit_map[y][x][:cur_position.index(idx+1)]
            elif(color_map[next_y][next_x] == 1) : #빨간색 판
                units.reverse()
                for i in units:
                    unit_map[next_y][next_x].append(i)
                    unit_data[i-1][0] = next_y
                    unit_data[i-1][1] = next_x
                unit_map[y][x] = unit_map[y][x][:cur_position.index(idx+1)]
            elif(color_map[next_y][next_x]==2 or next_y < 0 or next_y>=map_size or next_x<0 or next_x >= map_size):
                pass
            unit_data[idx][2] = direction
        if(len(unit_map[unit_data[idx][0]][unit_data[idx][1]])>=4):
            return 1
    return 0

### Main ###
map_size, unit_num = map(int,input().split())
color_map = []
unit_map = [[[] for i in range(map_size)]for j in range(map_size)]
dx = [1,-1,0,0]
dy = [0,0,-1,1] # 동서북남

for i in range(map_size):
    temp = list(map(int,input().split()))
    color_map.append(temp)

unit_data = []
for i in range(unit_num):
    temp = list(map(int,input().split()))
    temp[0] -= 1
    temp[1] -= 1
    temp[2] -= 1
    unit_data.append(temp)

for idx,value in enumerate(unit_data):
    unit_map[value[0]][value[1]].append(idx+1)

ans = 0
flag = 0
for i in range(1000):
    ans += 1
    if(move() == 1):
        flag = 1
        break

if(flag == 1):
    print(ans)
elif(flag == 0):
    print(-1)