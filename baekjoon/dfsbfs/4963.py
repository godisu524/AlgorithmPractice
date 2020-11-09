while True:
    m,n = map(int,input().split())
    if (n,m) == (0,0):
        break
    visited=[[False]*m for i in range(n)]
    array=[]
    for _ in range(n):
        array.append(list(map(int,input().split())))
    
    answer=0
    dx=[1,-1,0,0, 1,1,-1,-1]
    dy=[0,0,1,-1, 1,-1,1,-1]
    q=[]
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1 and not visited[i][j]:
                answer+=1
                q.append([i,j])        
                visited[i][j]=True
                while q:
                    now=q.pop(0)
                    for k in range(8):
                        nx = now[0]+dx[k]
                        ny = now[1]+dy[k]
                        if 0<=nx<n and 0<=ny<m and array[nx][ny]==1 and not visited[nx][ny]:
                            q.append([nx,ny])
                            visited[nx][ny]=True
    print(answer)


