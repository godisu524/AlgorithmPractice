#결국 다이나믹은 점화식을 세우는것.
n,m = map(int,input().split())
coins=[]
d = [10001]*10001
d[0] = 0
for _ in range(n):
    coins.append(int(input()))

for coin in coins:
    d[coin] =1

for i in range(n):
    for j in range(coins[i],m+1):
        if d[j-coins[i]] != 10001:
            #d[j]는 현재 위치까지 고려한이유가 2,3 의 최소공배수인 한 녀석이 이미 그자리를 꿰찻을수 있기 때문!
            d[j] = min(d[j],d[j-coins[i]]+1)
if d[m]!=10001:
    print(d[m])
else:
    print(-1)