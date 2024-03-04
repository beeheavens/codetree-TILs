def make_square(size):
    points = []
    dx = [1,-1,-1,1]
    dy = [-1,-1,1,1]
    for i in range(size):
        for j in range(size):
            start = [i,j]
            for k in range(size):
                second = [i+dy[0]*(k+1),j+dx[0]*(k+1)]
                if(0<=second[0]<size and 0<=second[1]<size):
                    for q in range(size):
                        third = [second[0]+dy[1]*(q+1),second[1]+dx[1]*(q+1)]
                        if(0<=third[0]<size and 0<=third[1]<size):
                            fourth = [third[0]+dy[2]*(k+1),third[1]+dx[2]*(k+1)]
                            if(0<=fourth[0]<size and 0<=fourth[1]<size):
                                points.append([start,second,third,fourth])
    return points

def cal(data):
    dx = [1,-1,-1,1]
    dy = [-1,-1,1,1]
    min_diff = -1
    for i in data:
        population = [0,0,0,0,0]
        tribe_map = [[0for j in range(map_size)]for k in range(map_size)]
        first = i[0]
        second = i[1]
        third = i[2]
        fourth = i[3]
        for k in range(map_size):
            for q in range(map_size):
                if(third[0]<k<first[0] and fourth[1]<q<second[1]):
                    tribe_map[k][q] = 1
        tribe_map[first[0]][first[1]] = 1
        tribe_map[second[0]][second[1]]=1
        tribe_map[third[0]][third[1]] = 1
        tribe_map[fourth[0]][fourth[1]] = 1
        left_flag = 2
        right_flag = 3
        for k in range(map_size):
            for q in range(map_size):
                if(tribe_map[k][q] == 0):
                    if(k<third[0] and q <= third[1]):
                        tribe_map[k][q] = 2
                    elif(third[0]<=k<fourth[0] and q<third[1]):
                        tribe_map[k][q] = 2
                    elif(k<third[0] and q>third[1]):
                        tribe_map[k][q] = 3
                    elif(third[0]<=k<=second[0] and third[1]<q):
                        tribe_map[k][q] = 3
                    elif(fourth[0]<=k and q<first[1]):
                        tribe_map[k][q] = 4
                    else:
                        tribe_map[k][q] = 5
        for k in range(map_size):
            for q in range(map_size):
                population[tribe_map[k][q]-1] += main_map[k][q]
        if(min_diff == -1):
            min_diff = max(population) -min(population)
        elif(min_diff > max(population)-min(population)):
            min_diff = max(population) - min(population)
    return min_diff
                    



map_size = int(input())
main_map = []

for i in range(map_size):
    temp = list(map(int,input().split()))
    main_map.append(temp)

point_data = make_square(map_size)
print(cal(point_data))