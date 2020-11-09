import sys
n=int(input())
a,b=map(int,input().split())

m = int(input())

visited=[False] * (n+1)
array=[[]for i in range(n+1)]
for _ in range(m):
    temp_x,temp_y = map(int,input().split())
    array[temp_x].append(temp_y)
    array[temp_y].append(temp_x)


q=[]
q.append(a)
visited[a]=True
count=0
while q:
    length = len(q)    
    for i in range(length):
        now=q.pop(0)
        if now == b:
            print(count)
            sys.exit()
        for num in array[now]:
            if not visited[num]:
                q.append(num)
                visited[num] = True
    count+=1
print(-1)