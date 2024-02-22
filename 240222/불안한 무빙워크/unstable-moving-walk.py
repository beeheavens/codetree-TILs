def move_moving_walk():
    temp = moving_walk[len(moving_walk)-1]
    del moving_walk[len(moving_walk)-1]
    moving_walk.insert(0,temp)
    if(moving_walk[length-1][0]==1):
        moving_walk[length-1][0] = 0
    
def move_person():
    for i in range(length-1,-1,-1):
        if(moving_walk[i][0]==1):
            if(moving_walk[i+1][0]==0 and moving_walk[i+1][1]>0):
                moving_walk[i][0] = 0
                moving_walk[i+1][0] = 1
                moving_walk[i+1][1] -= 1
                if(i+1 == length-1 and moving_walk[i+1][0] == 1):
                    moving_walk[i+1][0] = 0

def add_person():
    if(moving_walk[0][0] == 0 and moving_walk[0][1]>0):
        moving_walk[0][0] = 1
        moving_walk[0][1] -= 1

def check():
    checker = 0
    for i in moving_walk:
        if(i[1] == 0):
            checker += 1
    return checker
                
                

### main ###
length, finish_num = map(int,input().split())
moving_walk = list(map(int,input().split()))
for idx,value in enumerate(moving_walk):
    moving_walk[idx] = [0,value]

ans = 0
while(1):
    ans += 1
    move_moving_walk()
    move_person()
    add_person()
    if(check() >= finish_num):
        break
print(ans)