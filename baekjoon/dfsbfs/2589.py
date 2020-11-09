#bfs 인데 dfs 같으면서 bfs..
n,m = map(int,input().split())
array=[]
for i in range(n): 
    array.append(list(input()))
#print(array)

stack=[]
dx = [0, 0, 1, -1]
dy = [1, -1 , 0, 0]
ans=[]
for i in range(n):
    for j in range(m):
        if array[i][j]=="L":
            visited = [[False for i in range (m+1)] for j in range(n+1)]
            stack.append([i,j])
            visited[i][j] = True
            ans.append(-1)
            while stack:
                ans[-1]+=1
                length = len(stack)
                for _ in range(length):
                    now = stack.pop(0)
                    for k in range(4):
                        nx = now[0]+dx[k]
                        ny = now[1]+dy[k]
                        if 0<=nx<n and 0<=ny<m and array[nx][ny]!= "W" and not visited[nx][ny]:
                            stack.append([nx,ny])
                            visited[nx][ny]=True

                
print(max(ans))

                