N,M = map(int,input().split())
x,y,direction = map(int,input().split())
#방문햇는지를 알 맵. 초기화 코드 기억해놓을것.
d = [[0]*N for _ in range(M)]
d[x][y] =1
#[0,0,0,0]*4
_map=[]
#print(_map)
for _ in range(N):
    t_list =list(map(int,input().split()))
    _map.append(t_list)
#print(_map)
def check(n,m):
    if _map[n,m] ==0:
        return True
    else:
        return False
#뭔가할때 x 변화값, y 변화값 저장해놓기
#dx, dy
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
    global direction
    direction -=1
    if direction ==-1:
        direction = 3

count =1 
turn_time = 0

while True:
    ##방향 북
    turn_left()
    nx = x +dx[direction]
    ny = y +dy[direction]
    if d[nx][ny] ==0 and _map[nx][ny] == 0:
        d[nx][ny] =1 
        x= nx
        y= ny
        count +=1
        turn_time = 0
        continue
    else:
        turn_time +=1
    if turn_time == 4:
        nx = x -dx[direction]
        ny = y -dy[direction]
        if _map[nx][ny]==0:
            x = nx
            y = ny
        else:
            break
        turn_time=0
print(count)




