n,m = map(int,input().split())

array=[]
for _ in range(n):
    array.append(list(map(int,input().split())))

dx= [0,0,1,-1]
dy= [1,-1,0,0]


#check ices
def check_ice(array):
    visited=[[False for i in range(m+1)] for j in range(n+1)]
    q=[]
    count=0
    for i in range(n):
        for j in range(m):
            while q:
                now = q.pop(0)
                for k in range(4):
                    nx = dx[k]+now[0]
                    ny = dy[k]+now[1]
                    if 0<=nx<n and 0<=ny <m and array[nx][ny] != 0 and not visited[nx][ny]:
                        q.append([nx,ny])
                        visited[nx][ny] = True
            if array[i][j] != 0 and not visited[i][j] :
                count+=1
                q.append([i,j])
                visited[i][j]=True
    return count
years=0
while True:
    ices=[[False for _ in range(m+1)] for __ in range(n+1)]
    if check_ice(array)>=2:
        print(years)
        break
    elif check_ice(array) == 0:
        print(0)
        break
    else:
        for i in range(n):
            for j in range(m):
                if array[i][j] != 0 :
                    ices[i][j]= True
                    for k in range(4):
                        nx = dx[k]+i
                        ny = dy[k]+j
                        if 0<=nx<n and 0<=ny<m and array[nx][ny] == 0 and array[i][j]>=1 and not ices[nx][ny]:
                            array[i][j]-=1
        years+=1


    

        

