dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

beach = [[False] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
zone_num = 1
# 구역 이름 설정(DFS)
for r in range(N):
    for c in range(N):
        if MAP[r][c] and not visited[r][c]:
            visited[r][c] = True
            MAP[r][c] = zone_num
            stack = [(r, c)]
            while stack:
                y, x = stack.pop()
                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                        if MAP[ny][nx]:
                            visited[ny][nx] = True
                            MAP[ny][nx] = zone_num
                            stack.append((ny, nx))
                        else:
                            beach[y][x] = True
            zone_num += 1

# 구역 사이의 최단 거리(BFS)
result = float('inf')
for r in range(N):
    for c in range(N):
        if beach[r][c]:
            visited = [[False] * N for _ in range(N)]
            zone_num = MAP[r][c]
            visited[r][c] = True
            Q = [(r, c, 0)]
            sub_res = float('inf')
            while Q:
                print(Q)
                y, x, dist = Q.pop(0)
                
                if dist > result:
                    break

                if MAP[y][x] and MAP[y][x] != zone_num:
                    sub_res = dist -1
                    break

                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and MAP[ny][nx] != zone_num:
                        visited[ny][nx] = True
                        Q.append((ny, nx, dist + 1))
			# 결과 갱신
            if sub_res < result:
                result = sub_res
print(result)