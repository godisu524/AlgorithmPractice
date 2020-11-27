n= int(input())

array = list(map(int,input().split()))
#print(array)

dp = [0 for i in range(n+1)]
array.reverse()
array.insert(0,0)
#print(array)


for i in range(1,n+1):
    for j in range(1,i):
#        print(dp)
        if array[i] > array[i-j]:
            dp[i] = max(dp[i], dp[i-j])
    dp[i]+=1
print(max(dp))