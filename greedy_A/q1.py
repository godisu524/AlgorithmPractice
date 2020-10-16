n = int(input())
array = list(map(int, input().split()))

array.sort()

count = 0
power= 0
temp=0
for i in array:
    temp += i
    if temp >=n:
        count+=1
        temp = 0
        continue
    else:
        continue

print(count)
