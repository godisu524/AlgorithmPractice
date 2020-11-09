from collections import deque
#영역 찾기 BFS 
# dx[0], dy[0] => 오른쪽
# dx[1], dy[1] => 왼쪽
# dx[2], dy[2] => 아래
# dx[3], dy[3] => 위
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
#행렬 관게가 이상했다 ..
for _ in range(int(input())) :
    m,n,k = map(int,input().split())
    a=[[0 for i in range(m)] for j in range(n)]
    
    for _ in range(k):
        o,p= map(int,input().split())
        a[p][o] = 1
    q = deque()
    ans=0
    for i in range(n):
        for j in range(m):
            #print(i,j)
            if a[i][j] ==1:
                #print(a)
                #print(i,j)
                #print()
                a[i][j]=2
                q.append([i,j])
                ans+=1
                while q:            
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if a[nx][ny] == 1:
                                q.append((nx,ny))
                                a[nx][ny]=2
                
    
    print(ans)
    
    