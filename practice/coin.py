n,m = map(int,input().split())
array = []
for i in n:
    array.append(int(input()))

d = [10001] * 10001
for i in array:
    d[array[i]] = 1

for i in range(n):
    for j in range(array[i],m):
        if d[j-array[i]]!= 10001:
            d[j] = min(d[j],d[j-array[i]]+1)
if d[m]!= 10001:
    print(d[m])
else:
    print(-1)


