
TRY=int(input())

for _ in range(TRY):
    n= int(input())
    start=[0,0]
    end=[0,0]
    start[0],start[1]=map(int,input().split())
    end[0],end[1]=map(int,input().split())

    dx=[-2,-2,2,2,-1,-1,1,1]
    dy=[-1,1,-1,1,-2,2,2,-2]

    visited=[[False for i in range(n)] for _ in range(n)]

    array=[[0 for i in range(n)] for _ in range(n)]

    q=[]
    q.append(start)
    count=0
    while q:
        if end in q:
            print(count)
            break
        count+=1
        length=len(q)
        for _ in range(length):
            now= q.pop(0)
            for k in range(8):
                nx = now[0]+dx[k]
                ny= now[1]+ dy[k]
                if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny] =True
    

        