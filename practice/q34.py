#lis 문제.

n = int(input())

array = list(map(int,input().split()))

array.reverse()
dp=[1] * n
for i in range(1,n):
    for j in range(0,i):
        if array[i]> array[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp))