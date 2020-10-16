import heapq
import sys
input = sys.stdin.readline


def solution(n, s, a, b, fares):
    answers=[]

    INF = int(1e9)

    #노드의 개수, 간선

    m=len(fares)

    start = s

    graph = [[] for i in range(n+1)]

    visited = [False]* (n+1)

    distance = [INF] * (n+1)

    for fare in fares:
        graph[fare[0]].append((fare[1],fare[2]))
        graph[fare[1]].append((fare[0],fare[2]))
    #print(graph)
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
    answers.append(distance[a]+distance[b])

    first_distance=distance.copy()
    for i in range(1,n+1):
        temp = first_distance[i]
        visited = [False]* (n+1)
        distance = [INF] * (n+1)
        dijkstar(i)
        temp += distance[a]+distance[b]

        answers.append(temp)


    


    
    return min(answers)



print(solution(6,	4,	6,	2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))