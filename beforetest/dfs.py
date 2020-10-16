graph = []

n,m = map(int,input().split())
for _ in range(n):
    graph.append(list(map(int,input().split())))




def dfs(array, i, j):
    array[i][j] = 1
    for k in range(4):
        if array[dx[k]+]

#방향확인시
#     상  우  하  좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count =0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            count+=1