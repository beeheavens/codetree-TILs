def monster_copy(): # 몬스터의 알을 생성
    for monsters in monster_data:
        temp = []
        for i in range(3):
            temp.append(monsters[i])
        egg_data.append(temp)

def monster_move():
    #맵을 생성
    main_map = [[0 for i in range(4)] for j in range(4)]
    main_map[pac_pos[0]][pac_pos[1]] = 1
    for dead in dead_monsters:
        main_map[dead[0]][dead[1]] = 1
    # 갈 수 있는 곳은 0, 못가는 곳은 1
    for monsters in monster_data:
        direction = monsters[2]
        cur_y = monsters[0]
        cur_x = monsters[1]
        for i in range(8):
            actual_direction = direction + i
            if(actual_direction >=8):
                actual_direction -= 8
            next_y = cur_y+m_dy[actual_direction]
            next_x = cur_x+m_dx[actual_direction]
            if(0<=next_x<4 and 0<=next_y<4):
                if(main_map[next_y][next_x]==0):
                    monsters[0] = next_y
                    monsters[1] = next_x
                    monsters[2] = actual_direction
                    break

def pac_move():
    p_dx = [0,-1,0,1]
    p_dy = [-1,0,1,0]
    cur_y = pac_pos[0]
    cur_x = pac_pos[1]
    values = []
    main_map = [[0 for i in range(4)] for j in range(4)]
    for monsters in monster_data:
        main_map[monsters[0]][monsters[1]] += 1
    for a in range(4):
        for b in range(4):
            for c in range(4):
                first_y = cur_y + p_dy[a]
                first_x = cur_x + p_dx[a]
                second_y = first_y + p_dy[b]
                second_x = first_x + p_dx[b]
                third_y = second_y + p_dy[c]
                third_x = second_x + p_dx[c]
                if (first_y<0 or first_y>=4 or first_x<0 or first_x>=4):
                    continue
                if (second_y<0 or second_y>=4 or second_x<0 or second_x>=4):
                    continue
                if (third_y<0 or third_y>=4 or third_x<0 or third_x>=4):
                    continue
                eaten_monsters = 0
                eaten_monsters += main_map[first_y][first_x]
                eaten_monsters += main_map[second_y][second_x]
                if(first_y!=third_y or first_x != third_x):
                    eaten_monsters += main_map[third_y][third_x]
                values.append([eaten_monsters,a,b,c])
    values.sort(key=lambda x:(-x[0],x[1],x[2],x[3]))
    final_move = values[0]
    
    ret_monsters = []
    first_y = cur_y + p_dy[final_move[1]]
    first_x = cur_x + p_dx[final_move[1]]
    second_y = first_y + p_dy[final_move[2]]
    second_x = first_x + p_dx[final_move[2]]
    third_y = second_y + p_dy[final_move[3]]
    third_x = second_x + p_dx[final_move[3]]
    pac_pos[0] = third_y
    pac_pos[1] = third_x
    for monsters in monster_data:
        mon_y = monsters[0]
        mon_x = monsters[1]
        direction = monsters[2]
        if(mon_y == first_y and mon_x == first_x):
            dead_monsters.append([mon_y,mon_x,2])
            continue
        if(mon_y == second_y and mon_x == second_x):
            dead_monsters.append([mon_y,mon_x,2])
            continue
        if(mon_y == third_y and mon_x == third_x):
            dead_monsters.append([mon_y,mon_x,2])
            continue
        ret_monsters.append(monsters)
    return ret_monsters        
                
def vanish_dead():
    for data in dead_monsters:
        data[2] -= 1
    ret_arr = []
    for data in dead_monsters:
        if(data[2] == -1):
            continue
        ret_arr.append(data)
    return ret_arr            

def duplicate():
    for eggs in egg_data:
        monster_data.append(eggs)
    ret_arr =[]
    return ret_arr
### main ###
m_dx = [0,-1,-1,-1,0,1,1,1]
m_dy = [-1,-1,0,1,1,1,0,-1]

monster_num, turn_num = map(int,input().split())
pac_pos = list(map(int,input().split()))
pac_pos[0] -=1
pac_pos[1] -=1
monster_data = []
egg_data = []
dead_monsters = []
for i in range(monster_num):
    temp = list(map(int,input().split()))
    temp[0] -= 1
    temp[1] -= 1
    temp[2] -= 1
    monster_data.append(temp)

for i in range(turn_num):
    monster_copy()
    monster_move()
    monster_data = pac_move()
    dead_monsters = vanish_dead()
    egg_data = duplicate()

    

print(len(monster_data))