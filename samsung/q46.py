from collections import OrderedDict,deque

n = int (input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

fishes={}

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dist = [[-1]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            s_pos = [i,j] 
            graph[i][j]=0
            
        elif graph[i][j] != 0:
            if graph[i][j] in fishes.keys() :
                fishes[graph[i][j]].append([i,j])
            else:
                fishes[graph[i][j]]=[]
                fishes[graph[i][j]].append([i,j])

fishes =OrderedDict(sorted(fishes.items(), key=lambda t: t[0]))


def get_shortest(fishes,shark):
    short_score=[]
    for fish in fishes:
        fishx, fishy= fish[0], fish[1]
        sharkx, sharky = shark[0], shark[1]

        short_score.append((fish,abs(fishx-sharkx)+abs(fishy-sharky)))
    short_score.sort(key=lambda x:x[0][1])
    
    return min(short_score,key=lambda x:x[1])[0]
    #if short_score.count(min(short_score,key=lambda x:x[1])[0]) ==1:
    #    return min(short_score,key=lambda x:x[1])[0]
    #else:

def bfs():
    t_dist = [[-1]*n for _ in range(n)]
    tempq= deque([(s_pos[0],s_pos[1])])
    t_dist[s_pos[0]][s_pos[1]] = 0

    while tempq:
        #print(tempq)
        x, y = tempq.popleft() 

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <=nx and nx<n and 0<= ny and ny<n:
                if t_dist[nx][ny] == -1 and graph[nx][ny]<=baby_size:
                    t_dist[nx][ny] = t_dist[x][y]+1
                    tempq.append((nx,ny))
    return t_dist

        
def move_shark(s_pos,fish,graph,time):
    fishx, fishy= fish[0], fish[1]
    sharkx, sharky = s_pos[0], s_pos[1]

    tempq=[]
     
    

    return fish,time+abs(fishx-sharkx)+abs(fishy-sharky)
        
iter_size=1
baby_size=2
q=[]
total_time=0
while fishes:
    baby_ate =0
    
    if baby_size ==iter_size:
        print(iter_size)
        break


    while len(fishes[iter_size]) !=0:
        q.append(fishes[iter_size].pop(0))
    while len(q)!=0:    
        baby_ate+=1
        if baby_ate == baby_size:
            baby_size+=1
            baby_ate=0
        shortest_fish = get_shortest(q,s_pos)
        print(shortest_fish)
        q.remove(shortest_fish)
        dist=bfs()
        for d in dist:
            print(d)
        if dist[shortest_fish[0]][shortest_fish[1]] != -1:
            s_pos = shortest_fish
            total_time+=dist[shortest_fish[0]][shortest_fish[1]]
        print(s_pos,total_time)
    iter_size+=1
    




print(total_time)


print(s_pos)
print(fishes)






 