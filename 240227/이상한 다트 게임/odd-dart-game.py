def rotate(data):
    rotate_type = data[0] #회전할 원판
    direction = data[1] #방향
    distance = data[2] % num_numbers #회전 수
    for idx,value in enumerate(circle_data):
        if((idx+1)%rotate_type==0): #부합하는 원일 경우
            if(direction == 0): #시계 방향
                for i in range(distance):
                    circle_data[idx].insert(0,circle_data[idx][len(circle_data)-1]) #마지막을 앞으로 붙이고
                    del circle_data[idx][len(circle_data)-1] #마지막을 지우기
            elif(direction == 1): #반시계 방향
                for i in range(distance):
                    circle_data[idx].append(circle_data[idx][0])
                    del circle_data[idx][0]

def delete():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    del_flag = 0
    for i in range(num_circle):
        for j in range(num_numbers):
            if(circle_data[i][j] == -1):
                continue
            else:
                dfs = [[i,j]]
                path = []
                value = circle_data[i][j]
                while(len(dfs)>0):
                    path.append(dfs[0])
                    cur_y = dfs[0][0]
                    cur_x = dfs[0][1]
                    for k in range(4):
                        next_y = cur_y + dy[k]
                        next_x = cur_x + dx[k]
                        if(next_y<0):
                            continue
                        try:
                            if(circle_data[next_y][next_x]==value and [next_y,next_x] not in path and [next_y,next_x] not in dfs):
                                dfs.append([next_y,next_x])
                        except:
                            pass
                    del dfs[0]
                if(len(path)>1): #인접한게 있는 경우
                    for position in path:
                        circle_data[position[0]][position[1]] = -1
                        del_flag = 1
    if(del_flag==0): #정규화 해야함
        average = 0
        total = 0
        count = 0
        for i in range(num_circle):
            for j in range(num_numbers):
                if(circle_data[i][j] != -1):
                    total += circle_data[i][j]
                    count += 1
        average = total // count
        for i in range(num_circle):
            for j in range(num_numbers):
                if(circle_data[i][j] != -1):
                    if(circle_data[i][j] > average):
                        circle_data[i][j] -= 1
                    elif(circle_data[i][j] < average):
                        circle_data[i][j] += 1

        
                    
                            




### Main ###
num_circle, num_numbers, num_rotates = map(int,input().split())
circle_data = []
for i in range(num_circle):
    temp = list(map(int,input().split()))
    circle_data.append(temp)
rotate_data = []
for i in range(num_rotates):
    temp = list(map(int,input().split()))
    rotate_data.append(temp)

for i in rotate_data:
    rotate(i)
    delete()

ans = 0
for i in range(num_circle):
    for j in range(num_numbers):
        if(circle_data[i][j] != -1):
            ans += circle_data[i][j]
print(ans)