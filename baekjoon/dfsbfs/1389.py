n,m = map(int,input().split())
array=[[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    array[a].append(b)
    array[b].append(a)

ans = [[0] for _ in range(n+1)]
#print(ans)
for i in range(n+1):
    visited= [False]*(n+1)
    visited[i] = True
    q=[i]
    count=0
    while q: 
        length = len(q)
        count+=1
        for _ in range(length):
            now = q.pop(0)
            for node in array[now]:
                if not visited[node]:
                    q.append(node)
                    visited[node]= True
                    ans[i][0]+=count

print(ans.index(min(ans[1:])))

        



