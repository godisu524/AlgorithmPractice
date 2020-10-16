import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선

n,m = map(int, input().split())

start = 1

graph = [[] for i in range(n+1)]



distance = [INF] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

#for a in graph:
#    print(a)



def dijkstar(start):

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]< dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost< distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                    
dijkstar(start)

max_value = 0
max_distance = 0
result =[]
for i in range(1, n+1):
    if max_distance< distance[i]:
        max_value = i
        max_distance = distance[i]
        result = [max_value]
    elif max_distance == distance[i]:
        result.append(i)




print(max_value,max_distance,len(result))

