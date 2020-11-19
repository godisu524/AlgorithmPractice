n,k = map(int,input().split())
values=[]
for _ in range(n):
    values.append(int(input()))
    
dp =[0 for i in range(1000001)]
dp[0]= 1
for i in values:
    for j in range(1,k+1):
        dp[j]+=dp[j-i]
print(dp[k])