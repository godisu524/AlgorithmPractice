def dfs(graph,visited,v):
    print(v, end=" ")
    visited[v]=True
    try:
        for node in graph[v]:
            if not visited[node]:
                dfs(graph,visited,node)
    except:
        None


def bfs(graph,visited,v):
    visited[v]=True
    q=[]
    q.append(v)
    length=len(q)
    while q:
        #print(visited)
        for _ in range(length):
            temp=q.pop(0)
            print(temp,end=" ")
            for node in graph[temp]:
                if not visited[node]:
                    visited[node]=True
                    q.append(node)

                    
                    








n,m,v = map(int,input().split())

graph=[[]for _ in range(n+1)]
for i in range(m):
    start,to = map(int,input().split())
    graph[start].append(to)
    graph[to].append(start)

for i in range(len(graph)):
    graph[i].sort()
    


visited=[False for i in range(n+1)]

dfs(graph,visited.copy(),v)
print()
bfs(graph,visited.copy(),v)





    
