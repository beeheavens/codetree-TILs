student_num = int(input())

student_data = []
for i in range(student_num**2):
    data = list(map(int,input().split()))
    student_data.append(data)

main_map = [[0 for i in range(student_num)] for j in range(student_num)]

point_map = [[0 for i in range(student_num)] for j in range(student_num)]
for data in student_data:
    main_student = data[0] # map에 배치될 학생
    friend_map = [[0 for i in range(student_num)] for j in range(student_num)]
    empty_map = [[0 for i in range(student_num)] for j in range(student_num)]
    for column in range(student_num):
        for row in range(student_num):
            if(main_map[row][column] != 0):
                continue
            #동쪽
            if(column < student_num -1):
                if(main_map[row][column+1] == 0):
                    empty_map[row][column] += 1
                else:
                    if(main_map[row][column+1] in data):
                        friend_map[row][column] += 1
            #서쪽
            if(column > 0):
                if(main_map[row][column-1] == 0):
                    empty_map[row][column] += 1
                else:
                    if(main_map[row][column-1] in data):
                        friend_map[row][column] += 1
            #남쪽
            if (row < student_num -1):
                if(main_map[row+1][column] == 0):
                    empty_map[row][column] += 1
                else:
                    if(main_map[row+1][column] in data):
                        friend_map[row][column] += 1
            #북쪽
            if(row > 0):
                if(main_map[row-1][column] == 0):
                    empty_map[row][column] += 1
                else:
                    if(main_map[row-1][column] in data):
                        friend_map[row][column] += 1
    #여기까지 하면 해당 학생에 대한 friend_map과 empty_map 생성 완료!!
    #friend_map에서 좋아하는 친구가 많은 곳을 골라야함
    max_friend = 0
    max_position_num = 0
    target_row = 0
    target_column = 0
    for column in range(student_num):
        for row in range(student_num):
            if (friend_map[row][column] == max_friend):
                max_position_num += 1
                target_row = row
                target_column = column
            if (friend_map[row][column] > max_friend):
                max_friend = friend_map[row][column]
                max_position_num = 1
                target_row = row
                target_column = column
    if(max_position_num == 1): #좋아하는 친구의 수가 가장 많은 칸이 하나인 경우
        main_map[target_row][target_column] = main_student
        #point_map[target_row][target_column] = max_friend 오류가 있어서 폐기
        continue
    max_empty = 0
    max_empty_position_num = 0
    if(max_position_num > 1):
        for column in range(student_num):
            for row in range(student_num):
                if(friend_map[row][column] == max_friend): #1차 조건에 부합
                    if(empty_map[row][column]== max_empty):
                        max_empty_position_num += 1
                        target_row = row
                        target_column = column
                    if (empty_map[row][column] > max_empty):
                        max_empty = empty_map[row][column]
                        max_empty_position_num = 1
                        target_column = column
                        target_row = row
    #여기까지 오면 최대 친구 중 empty가 가장 많은 칸의 개수가 나온다!
    if(max_empty_position_num==1):
        main_map[target_row][target_column] = main_student
        #point_map[target_row][target_column] = max_friend 오류가 있어서 폐기
        continue
    if(max_empty_position_num > 1):
        flag = 0
        for row in range(student_num):
            for column in range(student_num):
                if (friend_map[row][column]==max_friend and empty_map[row][column]==max_empty and flag == 0 and main_map[row][column]==0):
                    main_map[row][column] = main_student
                    #point_map[row][column] = max_friend 오류가 있어서 폐기
                    flag = 1

    #여기까지 오면 다 넣음! 이제 점수계산

for column in range(student_num):
    for row in range(student_num):
        target_student = main_map[row][column]
        for data in student_data:
            if (data[0]==target_student): #우리가 찾는 그 학생!
                #동쪽
                if(column < student_num -1):
                    if(main_map[row][column+1] in data):
                        point_map[row][column] += 1
                #서쪽
                if(column > 0):
                    if(main_map[row][column-1] in data):
                        point_map[row][column] += 1
                #남쪽
                if (row < student_num -1):
                    if(main_map[row+1][column] in data):
                        point_map[row][column] += 1
                #북쪽
                if(row > 0):
                    if(main_map[row-1][column] in data):
                        point_map[row][column] += 1                

point = 0
for i in range(student_num):
    for j in range(student_num):
        if(point_map[i][j]== 0 ):
            continue
        else:
            point += 10 ** (point_map[i][j]-1)

print(point)