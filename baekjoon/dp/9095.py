t = int(input())
dp = [1, 2, 4]
for i in range(3, 10):
    dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])
for i in range(t):
    n = int(input())
    print(dp[n - 1])