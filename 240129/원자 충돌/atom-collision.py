def move():
    for i in atom_data:
        i[0] += i[3]*dy[i[4]]
        i[1] += i[3]*dx[i[4]]
        while(i[0]<0):
            i[0] += map_size
        while(i[0]>=map_size):
            i[0] -= map_size
        while(i[1]<0):
            i[1] += map_size
        while(i[1]>=map_size):
            i[1] -=  map_size

def synthesis():
    atom_map = [[[] for i in range(map_size)] for j in range(map_size)] # 질량 속력 방향
    num_map = [[0 for i in range(map_size)] for j in range(map_size)]
    ret = []
    for i in range(len(atom_data)):
        atom_map[atom_data[i][0]][atom_data[i][1]].append(i)
    for i in range(map_size):
        for j in range(map_size):
            if(len(atom_map[i][j])==1):
                ret.append(atom_data[atom_map[i][j][0]])
            if (len(atom_map[i][j]) > 1):
                mass= 0
                velocity = 0
                direction = 0
                last_dir = -1
                for data in atom_map[i][j]:
                    mass += atom_data[data][2]
                    velocity += atom_data[data][3]
                    if (last_dir == -1):
                        last_dir = atom_data[data][4]%2
                    elif(last_dir != atom_data[data][4]%2):
                        direction = 1
                if(mass // 5 == 0):
                    continue
                else:
                    mass = mass // 5
                    temp1 = [atom_data[data][0],atom_data[data][1],mass,velocity//len(atom_map[i][j])]
                    temp2 = [atom_data[data][0],atom_data[data][1],mass,velocity//len(atom_map[i][j])]
                    temp3 = [atom_data[data][0],atom_data[data][1],mass,velocity//len(atom_map[i][j])]
                    temp4 = [atom_data[data][0],atom_data[data][1],mass,velocity//len(atom_map[i][j])]
                    if (direction == 0):
                        temp1.append(0)
                        temp2.append(2)
                        temp3.append(4)
                        temp4.append(6)
                    elif(direction == 1):
                        temp1.append(1)
                        temp2.append(3)
                        temp3.append(5)
                        temp4.append(7)
                ret.append(temp1)
                ret.append(temp2)
                ret.append(temp3)
                ret.append(temp4)
    return ret

map_size, atom_num, time = map(int,input().split())

atom_data = []
for i in range(atom_num):
    temp = []
    temp = list(map(int,input().split()))
    temp[0] -= 1
    temp[1] -= 1
    atom_data.append(temp)

dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]

for i in range(time):
    move()
    atom_data = synthesis()

ans = 0
for i in atom_data:
    ans += i[2]

print(ans)