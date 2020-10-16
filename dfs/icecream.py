_map = [[1,1,1,0],
        [0,0,0,1],
        [1,1,0,0],
        [0,1,1,0]]

N = len(_map) 
M = len(_map[0])
#시작점에서 모든 방향 찾기. 
def dfs(x,y):
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False
    if _map[x][y] ==0:
        _map[x][y] =1
        dfs(x -1,y)
        dfs(x +1,y)
        dfs(x ,y-1)
        dfs(x ,y+1)
        return True
    return False

result =0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result+=1

print(result)

