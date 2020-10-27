import os
from copy import deepcopy
n, m = map(int,input().split())
array=[]

for i in range(m):
    array.append(list(map(int,(input().split()))))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count=0
while True:    
    last_array=deepcopy(array)
    for i in range(m):
        for j in range(n):
            if array[i][j]==1:
                for k in range(4):
                    nx=dx[k]+i
                    ny=dy[k]+j
                    if 0<=nx<m and 0<=ny<n and array[nx][ny]==0:
                        array[nx][ny]=2
    for i in range(m):
        for j in range(n):
            if array[i][j]==2:
                array[i][j]=1
    if last_array == array:
        break
    count+=1

for i in range(m):
    if 0 in array[i]:
        print(-1)
        os._exit(0)
print(count)




