from bisect import bisect_left, bisect_right

n = int(input())
result = -1
array = list(map(int,input().split()))
for i in range(n-1):
    if bisect_left(array,i) ==i:
        result = i
if n-1 == array[n-1]:
    result = n-1

print(result)