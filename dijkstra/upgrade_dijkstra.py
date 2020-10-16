import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선

n,m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n+1)]

visited = [False]* (n+1)

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

#for a in graph:
#    print(a)

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i]< min_value and not visited[i]:
            min_value = distance[i]
            index =i
    return index


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

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
