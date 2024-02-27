'''아 블록이 밑으로 떨어질 때 체크를 바닥부터 해서 위에 블럭이 있고 아래에 공간이 빈 경우에 그 안으로 들어가는 문제가 발생. 처음 설계를 잘못했다..
하지만 위에서부터 체크하면 밑에 아무것도 없을 때 블록이 아예 안놓여버림..'''
def put(block):
    type = block[0]
    block_y = block[1]
    block_x = block[2]
    #type 1. 한 칸 블록
    if(type == 1):
        flag = 0
        for i in range(6):
            if(yellow_table[i][block_x] == 1):
                yellow_table[i-1][block_x] = 1
                flag = 1
                break
        if(flag == 0):
            yellow_table[5][block_x] = 1
    #type 2. 가로로 두칸
    elif(type == 2): 
        first = 10
        second = 10#여기 이름을 어떻게 해야 편하지
        flag = 0
        #제일 작은 y값, 즉 어떤 y값에 블록이 위치하게 될지 결정
        for i in range(6):
            if(yellow_table[i][block_x]==1):
                first = i-1
                flag = 1
                break
        for i in range(6):
            if(yellow_table[i][block_x+1]==1):
                second = i-1
                flag = 1
                break
        if(flag == 1):
            pos_y = min(first,second)
            yellow_table[pos_y][block_x] = 1
            yellow_table[pos_y][block_x+1] = 1
        elif(flag == 0):
            yellow_table[5][block_x] = 1
            yellow_table[5][block_x+1] = 1
    elif(type == 3):
        flag = 0
        for i in range(6):
            if(yellow_table[i][block_x]==1):
                yellow_table[i-1][block_x] = 1
                yellow_table[i-2][block_x] = 1
                flag = 1
                break
        if (flag == 0):
            yellow_table[5][block_x] = 1
            yellow_table[4][block_x] = 1 
    
    #red table에 블록 쌓기
    block_x = 3-block[1]
    block_y = block[2]
    if(type == 1): #type 1
        flag = 0
        for i in range(6):
            if(red_table[i][block_x] == 1):
                red_table[i-1][block_x] = 1
                flag = 1
                break
        if(flag == 0):
            red_table[5][block_x] = 1
    elif(type == 3) : #type 3
        first = 10
        second = 10#여기 이름을 어떻게 해야 편하지
        flag = 0
        #제일 작은 y값, 즉 어떤 y값에 블록이 위치하게 될지 결정
        for i in range(6):
            if(red_table[i][block_x]==1):
                first = i-1
                flag = 1
                break
        for i in range(6):
            if(red_table[i][block_x-1]==1):
                second = i-1
                flag = 1
                break
        if(flag == 1):
            pos_y = min(first,second)
            red_table[pos_y][block_x] = 1
            red_table[pos_y][block_x-1] = 1
        elif(flag == 0):
            red_table[5][block_x] = 1
            red_table[5][block_x-1] = 1
    elif(type==2): #type 2
        flag = 0
        for i in range(6):
            if(red_table[i][block_x]==1):
                red_table[i-1][block_x] = 1
                red_table[i-2][block_x] = 1
                flag = 1
                break
        if (flag == 0):
            red_table[5][block_x] = 1
            red_table[4][block_x] = 1 
        

def boom():
    global score
    for i in range(5,-1,-1):
        if(yellow_table[i][0]==1 and yellow_table[i][1]==1 and yellow_table[i][2]==1 and yellow_table[i][3]==1): #한 줄이 채워지는 경우
            del yellow_table[i]
            yellow_table.insert(0,[0,0,0,0])
            score += 1
    for i in range(5,-1,-1):
        if(yellow_table[i][0]==1 and yellow_table[i][1]==1 and yellow_table[i][2]==1 and yellow_table[i][3]==1): #한 줄이 채워지는 경우
            del yellow_table[i]
            yellow_table.insert(0,[0,0,0,0])
            score += 1
    for i in range(5,-1,-1):
        if(red_table[i][0]==1 and red_table[i][1]==1 and red_table[i][2]==1 and red_table[i][3]==1): #한 줄이 채워지는 경우
            del red_table[i]
            red_table.insert(0,[0,0,0,0])
            score += 1
    for i in range(5,-1,-1):
        if(red_table[i][0]==1 and red_table[i][1]==1 and red_table[i][2]==1 and red_table[i][3]==1): #한 줄이 채워지는 경우
            del red_table[i]
            red_table.insert(0,[0,0,0,0])
            score += 1

def push():
    flag = 0
    for i in range(4):
        if(yellow_table[1][i]==1):
            flag += 1
            break
    for i in range(4):
        if(yellow_table[0][i]==1):
            flag +=1
            break
    for i in range(flag):
        del yellow_table[5]
        yellow_table.insert(0,[0,0,0,0])
    flag = 0
    for i in range(4):
        if(red_table[1][i]==1):
            flag += 1
            break
    for i in range(4):
        if(red_table[0][i]==1):
            flag +=1
            break
    for i in range(flag):
        del red_table[5]
        red_table.insert(0,[0,0,0,0])
            
num_block = int(input())
blocks = []
for i in range(num_block):
    temp = list(map(int,input().split()))
    blocks.append(temp)
global score
score = 0

yellow_table = [[0 for i in range(4)] for j in range(6)]
red_table = [[0 for i in range(4)]for j in range(6)]

for i in blocks:
    put(i)
    boom()
    push()
    #for j in yellow_table:
    #    print(j)
    #print("-------")
print(score)
checker = 0
for i in range(6):
    for j in range(4):
        if (yellow_table[i][j]==1):
            checker += 1
        if (red_table[i][j] == 1):
            checker += 1

print(checker)