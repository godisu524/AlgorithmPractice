import sys
n, m = map(int,input().split())
array=[]

for i in range(n):
    array.append(list(map(str,list(input()))))
    if "S" in array[-1]:
        start = [i,array[-1].index("S")]
    elif "D" in array[-1]:
        destination = [i,array[-1].index("D")]
#print(start,destination)

dx=[1,-1,0,0]
dy=[0,0,-1,1]
count=0

q=[start]
visited = [[False for __ in range(m+1)] for _ in range(n+1)]
#print(visited)
visited[start[0]][start[1]] = True

while q:
    #print(q)
    waters=[]
    for i in range(n):
        for j in range(m):
            if array[i][j] == "*":
                waters.append([i,j])
    for water in waters:
        for k in range(4):
            nx = dx[k]+water[0]
            ny = dy[k]+water[1]
            
            if 0<=nx<n and 0<=ny<m and array[nx][ny] =="."  :
                array[nx][ny]="*"


    count+=1
    length = len(q)
    
    for _ in range(length):
        now = q.pop(0)    
        for k in range(4):
            nx = dx[k]+now[0]
            ny = dy[k]+now[1]
            
            if 0<=nx<n and 0<=ny<m and array[nx][ny] in [".","D"] and not visited[nx][ny]:
                if array[nx][ny] == "D":
                    print(count)
                    sys.exit(0)
                else:
                    q.append([nx,ny])
                    visited[nx][ny] =True

print("KAKTUS")

        

