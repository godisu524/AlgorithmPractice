from collections import deque
def solution(graph):
    
    n = len(graph)
    m = len(graph)

   
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]


    def check_left(x,y,direction):
        if direction == 0:
            if graph[x][y+1] ==1:
                if graph[x+1][y] == 0:
                    return x+1,y,direction
                else:
                    direction +=1
                    if direction == 4:
                        direction =0
            else:
                direction +=1
                return x+dx[direction],y+dy[direction],direction
        if direction == 1:
            if graph[x-1][y] ==1:
                if graph[x][y+1] == 0:
                    return x,y+1,direction
                else:
                    direction +=1
                    if direction == 4:
                        direction =0
                        return x,y,direction
            else:
                return x+dx[direction],y+dy[direction],direction
        if direction == 2:
            if graph[x][y-1] ==1:
                if graph[x-1][y] == 0:
                    return x-1,y,direction
                else:
                    direction +=1
                    if direction == 4:
                        direction =0
                        return x,y,direction
            else:
                return x+dx[direction],y+dy[direction],direction
        if direction == 3:
            if graph[x+1][y] ==1:
                if graph[x][y-1] ==0:
                    return x,y-1,direction
                else:
                    if direction == 4:
                        direction =0
                        return x,y,direction
            else:
                return x+dx[direction],y+dy[direction],direction



    
    def bfs(x,y):
        direction=0
        answer = 0
        queue = deque()
        queue.append((x,y))
        while queue[-1] != (n-1,m-1):
            
            x,y = queue.popleft()
            print(x,y,direction)
            nx,ny,direction = check_left(x,y,direction)
            if nx<0 or ny<0 or nx>=n or ny>=m:
                queue.append((x,y))
                continue
            queue.append((nx,ny))
            
            answer +=1
        return answer
            

                    
                    
    print(bfs(0,0))

print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))
