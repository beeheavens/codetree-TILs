def bomb_set(): #폭탄 꾸러미를 만드는 함수
    set_map = [[0 for i in range(map_size)] for j in range(map_size)]
    set_ret = []
    for i in range(map_size):
        for j in range(map_size):
            if(main_map[i][j] != 0 and main_map[i][j] != -1 and set_map[i][j] == 0 and main_map[i][j] != -2): #조건에 부합하는 칸 dfs
                color = main_map[i][j] # 폭탄 색상
                red_bomb = 0
                bfs = [[i,j]]
                bomb_set = [[i,j]]
                while(len(bfs) > 0):
                    cur_y = bfs[0][0]
                    cur_x = bfs[0][1]
                    for k in range(4):
                        if(0<=cur_y + dy[k] and cur_y+dy[k] <map_size and 0<= cur_x + dx[k] and cur_x+dx[k] <map_size): #index 확인
                            if(main_map[cur_y+dy[k]][cur_x+dx[k]] == color and [cur_y+dy[k],cur_x+dx[k]] not in bomb_set): #같은색인경우
                                bfs.append([cur_y+dy[k],cur_x+dx[k]])
                                bomb_set.append([cur_y+dy[k],cur_x+dx[k]])
                                set_map[cur_y+dy[k]][cur_x+dx[k]] = 1
                            elif(main_map[cur_y+dy[k]][cur_x+dx[k]] == 0 and [cur_y+dy[k],cur_x+dx[k]] not in bomb_set) : #빨간색인 경우
                                bfs.append([cur_y+dy[k],cur_x+dx[k]])
                                bomb_set.append([cur_y+dy[k],cur_x+dx[k]])
                                red_bomb +=1
                    del bfs[0]
                ### 여기까지 bfs로 폭탄 묶음 구하기 성공. 쨔스 ! 이제 기준점을 구하자
                if(len(bomb_set) > 1): #한칸 짜리는 폭탄 묶음 취급 안함
                    temp = []
                    bomb_set.sort(key=lambda x :(-x[0], x[1])) #와 이거 초대박이다
                    for data in bomb_set:
                        if(main_map[data[0]][data[1]] == 0): #빨간 폭탄이면
                            continue
                        else:
                            temp.append(data)
                            break
                    temp.append(red_bomb)
                    temp.append(len(bomb_set))
                    set_ret.append(temp)
    return set_ret

def del_bomb():
    check_list.sort(key=lambda x :(-x[2],-x[1], -x[0][0],-x[0][1]))
    point = check_list[0][0] # 터트릴 폭탄 기준점
    bfs = [point]
    color = main_map[point[0]][point[1]]
    score = 0
    path = [[bfs[0][0],bfs[0][1]]]
    while(len(bfs) > 0):
        cur_y = bfs[0][0]
        cur_x = bfs[0][1]
        main_map[cur_y][cur_x] = -2
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if(0<=next_x and next_x<map_size and 0<=next_y and next_y<map_size):
                if(main_map[next_y][next_x] == color or main_map[next_y][next_x] == 0 ):
                    if([next_y,next_x] not in path and [next_y,next_x] not in bfs):
                        bfs.append([next_y,next_x])
                        path.append([next_y,next_x])
        del bfs[0]
        score += 1
    return score*score

def gravity():
    for i in range(map_size-1,0,-1):
        for j in range(map_size):
            if(main_map[i][j] == -2): #빈공간인 경우
                for k in range(i-1,-1,-1): #여기도 복습해야함
                    if(main_map[k][j]== -1): #돌이면
                        break
                    if(main_map[k][j] > -1):
                        main_map[i][j] = main_map[k][j]
                        main_map[k][j] = -2
                        break

def rotate():
    ret_arr = []
    for j in range(map_size-1,-1,-1):
        temp = []
        for i in range(map_size):
            temp.append(main_map[i][j])
        ret_arr.append(temp)
    return ret_arr
            


map_size, bomb_type = map(int,input().split())
main_map = [] # 빨간 폭탄 == 0 , 돌 == -1
dy = [0,1,0,-1]
dx = [1,0,-1,0]
for i in range(map_size):
    temp = list(map(int,input().split()))
    main_map.append(temp)

ans = 0
check_list = bomb_set()
while(len(check_list) > 0):
    ans += del_bomb()
    gravity()
    main_map = rotate()
    gravity()
    check_list = bomb_set()
print(ans)