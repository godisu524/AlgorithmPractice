from collections import deque, defaultdict
import math
import sys
sys.setrecursionlimit(10**6)
def find_parent(x, parent):
    if x == parent[x]:
        return x
    else:
        p = find_parent(parent[x], parent)
        parent[x] = p
        return p
def union_find(x, y, parent):
    x = find_parent(x, parent)
    y = find_parent(y, parent)
    parent[y] = x

def bfs(land, height, start, visited, group):
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    queue = deque()
    queue.append(start)
    while queue:
        y,x = queue.popleft()
        visited[y][x] = group
        for dy, dx in dirs:
            ny = y+dy
            nx = x+dx
            if 0<=ny<len(land) and 0<=nx<len(land[0]) and visited[ny][nx] == 0 and abs(land[y][x] - land[ny][nx]) <= height :
                visited[ny][nx] = group
                queue.append((ny,nx))
                
def find_height(land, height, table, visited):
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    for y in range(len(land)):
        for x in range(len(land[0])):
            if x+1<len(land[0]) and visited[y][x] != visited[y][x+1]:
                a,b = min(visited[y][x], visited[y][x+1]), max(visited[y][x], visited[y][x+1])
                table[(a,b)] = min(table[(a,b)], abs(land[y][x]-land[y][x+1]))
            if y+1<len(land[0]) and visited[y][x] != visited[y+1][x]:
                a,b = min(visited[y][x], visited[y+1][x]), max(visited[y][x], visited[y+1][x])
                table[(a,b)] = min(table[(a,b)], abs(land[y][x]-land[y+1][x]))

def find_parent(x, parent):
    if x == parent[x]:
        return x
    else:
        p = find_parent(parent[x], parent)
        parent[x] = p
        return p
                
def solution(land, height):
    answer = 0
    group = 1
    visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    for y in range(len(land)):
        for x in range(len(land[0])):
            if visited[y][x] == 0:
                bfs(land, height, (y,x), visited, group)
                group += 1
    table = defaultdict(lambda : math.inf)
    find_height(land, height, table, visited)
    table = sorted(table.items(), key = lambda x: x[1])
    
    cycle = {i:i for i in range(1,group)}
    for (a,b), value in table:
        # 사다리 연결
        if find_parent(a, cycle) != find_parent(b, cycle): # 사이클 방지
            union_find(a, b, cycle)
            answer += value
        # 모든 지형이 연결되었는지 확인
        if len(cycle.values()) == 1:
            return answer
    return answer