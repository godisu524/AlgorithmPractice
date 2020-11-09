from collections import deque

def solution(v):
    answer = [0,0,0]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    visited = [[False] * len(v) for _ in range(len(v[0]))]

    q=deque()
    for m in range(3):
        for i in range(len(v)):
            for j in range(len(v[0])):
                if m == v[i][j] and not visited[i][j]:
                    answer[m]+=1
                    q.append([i,j])
                    visited[i][j]=True
                    while q:
                        now=q.popleft()
                        for k in range(4):
                            nx = now[0]+dx[k]
                            ny = now[1]+dy[k]
                            if 0<=nx<len(v) and 0<=ny<len(v[0]) and not visited[nx][ny] and v[nx][ny] == m:
                                q.append([nx,ny])
                                visited[nx][ny]= True



       
    return answer




print(solution([[0,0,1],[2,2,1],[0,0,0]]))