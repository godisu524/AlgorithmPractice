INF = int(1e9)

n,m = map(int,input().split())

graph = [[INF]* (n+1) for _ in range(n+1)]
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    

#x,k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])


count=0
for a in graph:
    print(a)
for i in range(1,n+1):
    _flag =True
    for j in range(1,n+1):
        if graph[i][j] == INF and graph[j][i] == INF:
            _flag = False
    if _flag == True:
        count+=1
        print(i)
    else:
        _flag = True

print(count)