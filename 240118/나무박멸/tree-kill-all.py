def growth(): # 나무의 성장
    for column in range(size):
        for row in range(size):
            if main_map[row][column] > 0: # 나무가 있는 곳
                for d in range(4):
                    next_row = row + dy[d]
                    next_col = column + dx[d]
                    if 0<=next_row<size and 0<=next_col<size:
                        if main_map[next_row][next_col] >0:
                            main_map[row][column] += 1

def breeding(): # 나무의 번식
    breed_map = [[0 for i in range(size)] for j in range(size)]
    for column in range(size):
        for row in range(size):
            if main_map[row][column] > 0 : # 나무가 있는 곳
                empty_checker = 0
                for d in range(4):
                    next_row = row + dy[d]
                    next_col = column + dx[d]
                    if 0<=next_row<size and 0<=next_col<size: 
                        if main_map[next_row][next_col] == 0:
                            empty_checker += 1
                for d in range(4):
                    next_row = row + dy[d]
                    next_col = column + dx[d]
                    if 0<=next_row<size and 0<=next_col<size: 
                        if main_map[next_row][next_col] == 0:
                            breed_map[next_row][next_col] += (main_map[row][column]//empty_checker)
    
    for column in range(size):
        for row in range(size):
            main_map[row][column] += breed_map[row][column]
    
                
                                
def weeding(answer): # 제초
    weed_map = [[0 for i in range(size)] for j in range(size)]
    #제초제 지속기간 확인 먼저
    for column in range(size):
        for row in range(size):
            if main_map[row][column] < -2 : #제초제 지속중이면
                main_map[row][column] += 1
                if main_map[row][column] == -2 : #지속기간이 끝났다면
                    main_map[row][column] = 0
    for column in range(size):
        for row in range(size):
            if main_map[row][column] > 0 : #나무가 있는 곳
                weeded_trees = main_map[row][column] #제초될 나무 수
                for d in range(4): # 제초 방향
                    for r in range(weeding_range):
                        next_col = column + dx2[d]*(r+1)
                        next_row = row + dy2[d]*(r+1)
                        if (next_col < 0 or next_col >= size or next_row < 0 or next_row >= size):
                            break
                        elif(main_map[next_row][next_col] < 1 ): #index조건 먼저 체크해야 out of range 오류 안생김
                            break
                        if( main_map[next_row][next_col] > 0):
                            weeded_trees += main_map[next_row][next_col]
                weed_map[row][column] = weeded_trees
    max_weeded = 0
    max_weeded_row = 0
    max_weeded_column = 0
    for row in range(size):
        for column in range(size):
            if (max_weeded < weed_map[row][column]):
                max_weeded = weed_map[row][column]
                max_weeded_row = row
                max_weeded_column = column
    #제초될 곳을 결정했음!
    answer += max_weeded
    if(max_weeded == 0):
        return answer
    #print(main_map)
    #print(max_weeded_row)
    #print(max_weeded_column)
    #print(max_weeded)
    main_map[max_weeded_row][max_weeded_column] = -2 - weeding_period
    for d in range(4): # 제초 방향
        for r in range(weeding_range):
            next_col = max_weeded_column + dx2[d]*(r+1)
            next_row = max_weeded_row + dy2[d]*(r+1)
            if (next_col < 0 or next_col >= size or next_row < 0 or next_row >= size):
                break
            elif(main_map[next_row][next_col] < 1): #index조건 먼저 체크해야 out of range 오류 안생김
                if(main_map[next_row][next_col]!= -1):
                    main_map[next_row][next_col] = -2 - weeding_period
                break
            if( main_map[next_row][next_col] > 0):            
                main_map[next_row][next_col] = -2 - weeding_period
    return answer
    
    
                    
                

####*******main*******####
data = list(map(int,input().split()))
size = data[0]  #map 크기
period = data[1] # 박멸 기간
weeding_range = data[2] # 제초제 범위
weeding_period = data[3] # 제초제 기간
dx = [1,-1,0,0]
dy = [0,0,1,-1]

dx2 = [1,1,-1,-1]
dy2 = [-1,1,1,-1]

main_map = [] # main map

for i in range(size):
    line = list(map(int,input().split()))
    main_map.append(line)

#여기까지가 준비 과정


ans = 0
for year in range(period):
    growth()
    breeding()
    ans = weeding(ans)
print(ans)