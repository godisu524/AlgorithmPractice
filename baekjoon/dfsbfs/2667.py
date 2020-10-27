from collections import deque
#영역 찾기 BFS 
# dx[0], dy[0] => 오른쪽
# dx[1], dy[1] => 왼쪽
# dx[2], dy[2] => 아래
# dx[3], dy[3] => 위
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
 
n= int(input())
a = [list(map(int, list(input()))) for _ in range(n)]
q = deque()


ans=0
ans_count=[]

for i in range(n):
    for j in range(n):
        if a[i][j] ==1:
            a[i][j]=2
            count=0
            q.append([i,j])
            ans+=1
            while q:
                count+=1
                #print(q)
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if a[nx][ny] == 1:
                            q.append((nx,ny))
                            a[nx][ny]=2
            ans_count.append(count)
ans_count.sort()
print(ans)
for a in ans_count:
    print(a)




