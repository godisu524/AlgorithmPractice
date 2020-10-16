n,m = map(int,input().split())


graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))



dp =[[0 for _ in range(m)] for i in range(n)]

print(dp)

for i in range(n):
    dp[i][0]= graph[i][0]
for a in graph:
    print(a)
for j in range(1,m):
    for i in range(n):
        if i  ==0 :
            dp[i][j]= max(dp[i][j-1],dp[i+1][j-1])+graph[i][j]
        elif i == n-1:
            dp[i][j]= max(dp[i][j-1],dp[i-1][j-1])+graph[i][j]
        else:
            print(i,j)
            dp[i][j]= max(dp[i][j-1],dp[i-1][j-1],dp[i+1][j-1])+graph[i][j]
            if (i,j) == (2,2):
                print(max(dp[i][j-1],dp[i-1][j-1],dp[i+1][j-1]))
                print(dp[i+1][j-1])


for a in dp:
    print(a)





