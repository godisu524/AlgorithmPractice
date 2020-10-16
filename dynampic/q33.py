n = int(input())

t = [0]*n
p = [0]*n
dp = [0] * (n+1)

for _ in range(n):
    t[_],p[_] = map(int,input().split())

max_value = 0
time = 0

for i in range(n-1, -1, -1):
    time = t[i]+ i
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
    
print(max_value)



