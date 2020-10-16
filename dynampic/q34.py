n = int(input())

array = list(map(int,input().split()))
array.reverse()
dp = [1]* n

#lis 인데 이걸 이해해야 넘어갈수있다.

for i in range(1,n):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)
#그니까 시작점을 다르게해서 어차피 만약시작점이 낮은곳이 더크면 그게 더 큰 lis 가되는거라 상관없음 그냥 다 비교만해주면된다..

print(n-max(dp))