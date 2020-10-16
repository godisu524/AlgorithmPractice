import sys

n = int(input())
a = int(input())

array = [[0]*n for _ in range(n+1)]
apples=[]
for _ in range(a):
    x,y = map(int, input().split())
    array[x][y] = 1

t = int(input())
turns = {}
for _ in range(t):
    x,y = input().split()
    x= int(x)
    turns[x] = y

head = [1,1]
#    L U R D
dx =[0,-1,0,1]
dy =[-1,0,1,0]

body = []
body.append(head.copy())
direction = "R"

time =0
while True:
    if time in turns:
        direction = turns[time]
    temp = head.copy()

    if direction == "R":
        head[0] +=dx[2] 
        head[1] +=dy[2]
    elif direction == "L":
        head[0] +=dx[0] 
        head[1] +=dy[0]
    elif direction == "U":
        head[0] +=dx[1] 
        head[1] +=dy[1]
    elif direction == "D":
        head[0] +=dx[3] 
        head[1] +=dy[3]
    print(time)
    print("head: ",head)
    print("body: ", body)
    
    if head[0]>n or head [0] <1 or head[1]>n or head[1] <1:
        print(head)
        print(time)
        sys.exit(1)


   


    if head in body:
        print("ohno")
        print(time)

        sys.exit(1)

    if array[head[0]][head[1]] != 1:
        time +=1 
        body.pop()
        body.insert(0,head.copy())
        
    else :
        time+=1
        body.insert(0,head.copy())








