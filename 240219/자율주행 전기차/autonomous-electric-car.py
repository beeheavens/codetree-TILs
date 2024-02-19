def shortest_path():
    car_y = car[0]
    car_x = car[1]
    distance_map = [[0 for i in range(map_size)] for j in range(map_size)]
    for i in range(map_size):
        for j in range(map_size):
            if(main_map[i][j]==1):
                distance_map[i][j] = -1
    bfs = [[car_y,car_x]]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    count = 0
    while(1):
        temp = []
        while(len(bfs)!=0):
            cur_y = bfs[0][0]
            cur_x = bfs[0][1]
            distance_map[cur_y][cur_x] = count
            for i in range(4):
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]
                if(0<=next_y<map_size and 0<=next_x<map_size and main_map[next_y][next_x]!= 1 and distance_map[next_y][next_x]==0 and [next_y,next_x] not in temp):
                    if(next_y == car_y and next_x==car_x):
                        continue
                    else:
                        temp.append([next_y,next_x])
            del bfs[0]
        if(len(temp) == 0):
            break
        count += 1
        bfs = temp
    return distance_map

def move():
    min_dis = map_size * map_size
    index = 0
    for idx,value in enumerate(person_data):
        person_y = value[0]
        person_x = value[1]
        if(min_dis > distance[person_y][person_x]):
            min_dis = distance[person_y][person_x]
            index = idx
        elif(min_dis == distance[person_y][person_x]):
            temp_y = person_data[index][0]
            if(temp_y > person_y):# 더 위에 있는 경우
                min_dis = distance[person_y][person_x]
                index = idx
            elif(temp_y == person_y):
                temp_x = person_data[index][1]
                if(temp_x > person_x):
                    min_dis = distance[person_y][person_x]
                    index = idx
    #이제 index 변수는 최단 거리 사람의 person data 내 idx값임
    if(min_dis==0 and [car[0],car[1]] != [person_data[index][0],person_data[index][1]]):
        return -1
    if(min_dis>car[2]): #배터리가 없어서 못가는 경우
        return -1
    else:
        car[0] = person_data[index][0]
        car[1] = person_data[index][1]
        #이동
        car[2] -= min_dis
        return index

def move_dest(index):
    dest_y = person_data[index][2]
    dest_x = person_data[index][3]
    if(car[2] < distance[dest_y][dest_x]):
        return -1
    else:
        car[0] = dest_y
        car[1] = dest_x
        car[2] += distance[dest_y][dest_x]
        del person_data[index]
        return 1
    

### main ###
map_size, num_person, battery = map(int,input().split())
main_map = []
for i in range(map_size):
    main_map.append(list(map(int,input().split())))

car = list(map(int,input().split()))
car[0] -= 1
car[1] -= 1
car.append(battery)
person_data = []
for i in range(num_person):
    temp = list(map(int,input().split()))
    for k in range(4):
        temp[k] -= 1
    person_data.append(temp)

distance = [[0 for i in range(map_size)] for j in range(map_size)]
result = 0
flag = 0

## main loop ##
while(len(person_data)>0):
    distance = shortest_path()
    result = move()
    if (result == -1):
        print("-1")
        flag = 1
        break
    distance = shortest_path()
    result = move_dest(result)
    if (result == -1):
        print("-1")
        flag = 1
        break

if(flag != 1):
    print(car[2])