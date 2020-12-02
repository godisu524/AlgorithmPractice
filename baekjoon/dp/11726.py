
n = int(input())


dp = [0 for i in range(n+1)]

dp[0]= 1
dp[1]= 1
dp[2]= 2


if n <=2:
    print(dp[n])
else:
    for i in range(3,n+1):
        dp[i] = (dp[i-2]+dp[i-1])%10007
    
    print(dp[n])