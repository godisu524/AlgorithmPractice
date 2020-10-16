a,n = map(str,input().split())
a = ord(a)-ord('a') +1
n = int(n)
print(a,n)
count=0
ways=[[2,1],[2,-1],[1,2],[1,-2],[-1,-2],[-2,-1],[-1,2],[-2,1]]
for way in ways:
    if a+way[0] in range(1,9):
        if n+way[1] in range(1,9):
            count +=1

print(count)