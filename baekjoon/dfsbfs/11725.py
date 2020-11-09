import sys
input = sys.stdin.readline
n = int(input())

ans=[[]for i in range(n+1)]
array = [[] for i in range(n+1)]
visited= [False for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    array[a].append(b)
    array[b].append(a)




stack = [1]

#print(count)
while stack:

    
    temp = stack.pop()
    for i in array[temp]:
        
        if not visited[i]:
            ans[i] = temp
            stack.append(i)        
            visited[i] = True
            
#print(array)
for i in ans[2:]:
    print(i)



    
