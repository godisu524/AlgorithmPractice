n = int(input())

array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy= [0,0,-1,1]
counts=[]
for  i in range(0,100):
    count=0
    drown=[[False for _ in range(n+1)] for __ in range(n+1)]
    visited=[[False for _ in range(n+1)] for __ in range(n+1)]
    #initialize
    for q in range(n):
        for w in range(n):
            if array[q][w]  <=i:
                drown[q][w] = True

    

    for st in range(n):
        for ed in range(n): 
            if not drown[st][ed] and not visited[st][ed]:
                count+=1
                stack=[[st,ed]]
                visited[st][ed] = True
                while stack:
                    temp = stack.pop()
                    for k in range(4):
                        nx= temp[0]+dx[k]
                        ny= temp[1]+dy[k]
                        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and not drown[nx][ny]:
                            stack.append([nx,ny])
                            visited[nx][ny] =True
                
                
    counts.append(count)

print(max(counts))
                
                
