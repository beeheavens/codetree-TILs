def runner_run():
    for i in runner_data:
        distance = abs(i[0] - catcher_data[0]) + abs(i[1] - catcher_data[1])
        if(distance <4): #술래와의 거리 3 이하
            if(0<=i[0]+dy[i[2]]<map_size and 0<=i[1]+dx[i[2]]<map_size):# index 체크
                if(i[0]+dy[i[2]] == catcher_data[0] and i[1]+dx[i[2]]== catcher_data[1]):
                    continue
                else:
                    i[0] += dy[i[2]]
                    i[1] += dx[i[2]]
            else:
                if(i[2] == 1): i[2] = 0
                elif(i[2] == 0): i[2] =1
                elif(i[2] == 2): i[2] =3
                elif(i[2] == 3): i[2] =2
                if(0<=i[0]+dy[i[2]]<map_size and 0<=i[1]+dx[i[2]]<map_size):# index 체크
                    if(i[0]+dy[i[2]] == catcher_data[0] and i[1]+dx[i[2]]== catcher_data[1]):
                        continue
                    else:
                        i[0] += dy[i[2]]
                        i[1] += dx[i[2]]

def catcher_move():
    #바깥으로 이동
    if(catcher_data[6]==0):
        catcher_data[0]+= c_dy[catcher_data[2]]
        catcher_data[1]+= c_dx[catcher_data[2]]
        catcher_data[3] += 1 # 이동횟수 +1
        if (catcher_data[3]==catcher_data[4]):
            catcher_data[3] = 0
            catcher_data[2] = (catcher_data[2]+1)%4 # direction 변경
            catcher_data[5] += 1
            if(catcher_data[5] == 2): #limitation 한계 도착
                catcher_data[5] = 0
                catcher_data[4] += 1
        if(catcher_data[0] == 0 and catcher_data[1]==0): #끝에 도착
            catcher_data[6] = 1
            catcher_data[5] = -1
            catcher_data[2] = 1
            catcher_data[4] -= 1
            catcher_data[3] = 0
    elif(catcher_data[6]==1):
        catcher_data[0]+= c_dy[catcher_data[2]]
        catcher_data[1]+= c_dx[catcher_data[2]]
        catcher_data[3] += 1 # 이동횟수 +1
        if (catcher_data[3]==catcher_data[4]):
            catcher_data[3] = 0
            catcher_data[2] = (catcher_data[2]+3)%4 # direction 변경
            catcher_data[5] += 1
            if(catcher_data[5] == 2): #limitation 한계 도착
                catcher_data[5] = 0
                catcher_data[4] -= 1
        if(catcher_data[0] == center and catcher_data[1]==center): #가운데 도착
            catcher_data[6] = 0
            catcher_data[5] = 0
            catcher_data[2] = 3
            catcher_data[4] = 1
            catcher_data[3] = 0

def catch(turn):
    del_target = []
    for i in range(3):
        target_y = catcher_data[0] + c_dy[catcher_data[2]]*i
        target_x = catcher_data[1] + c_dx[catcher_data[2]]*i
        temp = [target_y,target_x]
        if(temp in tree_data): #이거 잘 작동하려나?
            continue
        for j in range(len(runner_data)):
            if(runner_data[j][0] == target_y and runner_data[j][1] == target_x):
                del_target.append(j)
    del_target.sort()
    ans = turn*len(del_target)
    for i in range(len(del_target)):
        del runner_data[del_target[i]-i]            
    return ans
    

map_size, runner_num, tree_num, turn_num = map(int,input().split())
runner_data = [] # y , x, direction
tree_data = [] # y, x
for i in range(runner_num):
    temp = list(map(int,input().split()))
    temp[0] -= 1
    temp[1] -= 1
    runner_data.append(temp)
for i in range(tree_num):
    temp = list(map(int,input().split()))
    temp[0] -= 1
    temp[1] -= 1
    tree_data.append(temp)
#준비완료

dx = [-1,1,0,0]# 1 오른쪽, 0 왼쪽
dy = [0,0,1,-1]# 2 아래, 3 위

c_dx = [1,0,-1,0]
c_dy = [0,1,0,-1]

center = map_size // 2
catcher_data = [map_size//2,map_size//2,3,0,1,0,0] #술래 위치, direction, 반복횟수, limitation, limation반복횟수, 바깥or안

ans = 0
for i in range(turn_num):
    runner_run()
    catcher_move()
    ans += catch(i+1)
print(ans)