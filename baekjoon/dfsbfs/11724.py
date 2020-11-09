n,m=map(int,input().split())

array=[[] for i in range(n+1)]
start=0
for i in range(m):
    a ,b = map(int,input().split())
    array[a].append(b)
    array[b].append(a)


answer=0
visited=[False] * (n+1)

q=[]
for i in range(1,n+1):
    if not visited[i]:
        q.append(i)
        visited[i]=True
        while q:
            print(q)
            now=q.pop(0)
            for node in array[now]:
                if not visited[node]:
                    q.append(node)
                    visited[node]=True
        answer+=1
print(answer)






