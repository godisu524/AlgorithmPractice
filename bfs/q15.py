from collections import deque
n,m,k,x = map(int,input().split())

visited=[]
q = deque()
array = [[0] for _ in range(n+1)] 
for i in range(m):
    a,b = map(int,input().split())
    array[a].append(b)
    array[b].append(a)
dist = 1

visited.append(x)
for i in array[x][1:]:
    q.append(i)
    visited.append(i)


while dist != k:
    length = len(q)
    for i in range(length):
        a = q.popleft()
        visited.append(a)
        for index in array[a][1:]:
            if index not in visited:
                q.append(index)
    dist+=1

if len(q) != 0:
    for i in q:
        print(i)
else:
    print(-1)

    

