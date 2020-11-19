import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

dp = [[-1 for _ in range(n)] for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def dfs(sy, sx):
    print('---------')
    for s in dp:
        print(s)
    dp[sy][sx] = 0
    lst = []
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if 0 <= nx < n and 0 <= ny < n:
            if mat[sy][sx] < mat[ny][nx]:
                if dp[ny][nx] == -1:
                    dfs(ny, nx)
                lst.append(dp[ny][nx])
    if lst:
        dp[sy][sx] = max(lst) + 1
    else:
        dp[sy][sx] = 1

ans = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            dfs(i, j)
for s in dp:
    ans = max(ans, max(s))
print(ans)