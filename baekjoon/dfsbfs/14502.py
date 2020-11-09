from itertools import combinations
from copy import deepcopy
n, m = map(int,input().split())
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

def bfs(array):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    visited=[[False]*m for i in range(n)]
    q=[]
    for i in range(n):
        for j in range(m):
            if array[i][j]==2:
                q.append([i,j])
                while q:
                    now=q.pop(0)
                    visited[now[0]][now[1]] = True
                    for k in range(4):
                        nx = now[0]+dx[k]
                        ny = now[1]+dy[k]
                        if 0<=nx<n and 0<=ny<m and array[nx][ny] ==0 and not visited[nx][ny]:
                            array[nx][ny]=2
                            q.append([nx,ny])
    count=0
    #print(array)
    for i in range(n):
        for j in range(m):
            if array[i][j]==0:
                count+=1
    return count
    

max_answer=0
zeros=[]
for i in range(n):
    for j in range(m):
        if array[i][j]==0:
            zeros.append([i,j])


for comb in combinations(zeros,3):
    temp_array=deepcopy(array)
    for c in comb:
        temp_array[c[0]][c[1]] = 1
    max_answer=max(max_answer,bfs(temp_array))
                
print(max_answer)