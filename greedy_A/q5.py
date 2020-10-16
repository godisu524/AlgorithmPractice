n, m = map(int,input().split())

numbers = list(map(int,input().split()))

count= 0

for i in range(n-1):
    for j in range(i,n):
        if numbers[i] != numbers[j]:
            count +=1
print(count)


