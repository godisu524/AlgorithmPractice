from collections import deque

N,M,K,X = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)


q=[X]
count=0
distance = [-1 for _ in range(N+1)]
print(distance)
distance[X] = 0
while q:
    now = q.pop(0)
    print(q)
    for node in graph[now]:
        if distance[node] == -1:
            distance[node] = distance[now] +1
            q.append(node)
print(distance)
answer=[]
for i in range(len(distance)):
    if distance[i] == K:
        answer.append(i)

if len(answer) != 0:
    print(answer)
else:
    print(-1)




#print(count)



