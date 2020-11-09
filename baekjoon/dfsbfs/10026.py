n = int(input())
array=[]
for i in range(n):
    array.append(list(input()))

dx=[1,-1,0,0]
dy=[0,0,-1,1]

visited= [[False]*n for i in range(n)]

q=[]
last_color="Z"
first_answer=0
second_answer=0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            last_color = array[i][j]
            q.append([i,j])
            first_answer+=1
            visited[i][j]=True
            while q:
                #print(q)
                now = q.pop(0)
                for k in range(4):
                    nx=now[0]+dx[k]
                    ny=now[1]+dy[k]
                    if 0<=nx<n and 0<=ny<n and array[nx][ny]==last_color and not visited[nx][ny]:
                        q.append([nx,ny])
                        visited[nx][ny]=True
        



for i in range(n):
    for j in range(n):
        if array[i][j] == "R":
            array[i][j]= "G"
visited= [[False]*n for i in range(n)]   
last_color="Z"
for i in range(n):
    for j in range(n):
        if  not visited[i][j]:
            last_color = array[i][j]
            q.append([i,j])
            second_answer+=1
            visited[i][j]=True
            while q:
                #print(q)
                now = q.pop(0)
                for k in range(4):
                    nx=now[0]+dx[k]
                    ny=now[1]+dy[k]
                    if 0<=nx<n and 0<=ny<n and array[nx][ny]==last_color and not visited[nx][ny]:
                        q.append([nx,ny])
                        visited[nx][ny]=True
        
            
print(first_answer,second_answer)