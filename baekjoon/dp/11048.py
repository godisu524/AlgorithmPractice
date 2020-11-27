n, m = map(int,input().split())
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))



dp = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1],dp[i][j-1]) + array[i-1][j-1]


print(dp[n][m]) 

        
