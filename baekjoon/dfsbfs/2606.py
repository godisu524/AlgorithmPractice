n=int(input())
m=int(input())



array=[[] for i in range(n+1)]
visited=[False] * (n+1)



for i in range(m):
    m,v=map(int,input().split())
    array[m].append(v)
    array[v].append(m)

q=[]
q.append(1)
visited[1]=True
count=0

while q:
    length= len(q)
    for i in range(length):
        now=q.pop(0)
        for j in array[now]:
            if not visited[j]:
                q.append(j)
                visited[j]= True
                count+=1
print(count)


