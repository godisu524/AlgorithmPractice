graph = [[1, 2, 3, 4],
[0, 0, 0, 5],
[9, 8, 7, 6]]


dp = [[0 for _ in range(len(graph[0])+1)] for _ in range(len(graph)+1)]

for i in range(1,len(graph)+1):
    #print(dp)
    for j in range(1,len(graph[0])+1):
        print(dp)
        dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) +graph[i-1][j-1]


print(dp)