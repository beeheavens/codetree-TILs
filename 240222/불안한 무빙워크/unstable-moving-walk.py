def move_moving_walk():
    temp = moving_walk[len(moving_walk)-1]
    del moving_walk[len(moving_walk)-1]
    moving_walk.insert(0,temp)
    for idx,value in enumerate(person_data):
        person_data[idx] += 1
    try:
        if(person_data[0]==length):
            moving_walk[person_data[0]][1] = 0
            del person_data[0]
    except:
        pass

def move_person():
    for idx, value in enumerate(person_data):
        if(moving_walk[value+1][0]!=0 and moving_walk[value+1][1]==0):
            index = value + 1
            moving_walk[value][1] = 0
            person_data[idx] += 1
            moving_walk[index][1] = 1
            moving_walk[index][0] -= 1
    try:
        if(person_data[0] == length):
            moving_walk[person_data[0]][1] = 0
            del person_data[0]
    except:
        pass

def add_person():
    if(moving_walk[0][0]!=0 and moving_walk[0][1]==0):
        moving_walk[0][1] = 1
        moving_walk[0][0] -= 1
        person_data.append(0)

def check():
    num = 0
    for i in moving_walk:
        if(i[0]==0):
            num += 1
    if(num>=finish_num):
        return True
    else:
        return False

### main ###
length, finish_num = map(int,input().split())
moving_walk = list(map(list,input().split()))
for i in moving_walk:
    i[0] = int(i[0])
    i.append(0)
global person_data
person_data = []

ans = 0
while(1):
    ans += 1
    move_moving_walk()
    move_person()
    add_person()
    if(check()):
        break
    

print(ans)