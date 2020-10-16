n,k = map(int,input().split())

array = [[k+1,k+1,k+1]]
for i in range(n):
    array.append(list(map(int, input().split())))

s,x,y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


virus_list= []
for time in range(s):
    
    for virus in range(1,k+1):
        virus_list.clear()
        for i in range(1,n+1):
            for j in range(n):
                if virus == array[i][j]:
                    virus_list.append([i,j])
        print(virus, virus_list)
        for vl in virus_list:
            for m in range(4):
                if vl[0]+dx[m] in range(1,n+1) and vl[1]+dy[m] in range(0,n):
                    if array[vl[0]+dx[m]][vl[1]+dy[m]] == 0: 
                        array[vl[0]+dx[m]][vl[1]+dy[m]] = virus
                
    for a in array:
        print(a)
    print()
    
    

print(array[x][y-1])

