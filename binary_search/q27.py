from bisect import bisect_left, bisect_right
n,x = map(int,input().split())

array = list(map(int,input().split()))

a = bisect_left(array,x+1) 
b= bisect_right(array,x-1)

if a - b >= 1:
    print(a-b)
else:
    print(-1)
