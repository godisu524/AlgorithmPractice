n = int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            up_left=0
        else:
            up_left = graph[i-1][j-1]
        if j ==i:
            up_right = 0
        else:
            up_right = graph[i-1][j]
        graph[i][j] = max(up_left,up_right) + graph[i][j]
    
print(graph)
print(max(graph[-1]))
