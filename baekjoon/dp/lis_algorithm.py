#sum
n = int(input())

array = [0] + list(map(int,input().split()))

dp = [x for x in array]

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j]+array[i])
print(max(dp))




"""

#length 요놈이 중요하다.
n= int(input())
array = [0]+list(map(int,input().split()))

dp = [0] *(n+1)

for i in range(1,n+1):
    for j in range(1,i):
        if array[i] > array[i-j]:
            dp[i] = max(dp[i],dp[i-j])
    dp[i]+=1
print(max(dp))
"""