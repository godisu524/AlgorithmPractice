import math
def solution(a):
    answer = 0
    left, right = math.inf, math.inf
    
    maps = [[0 for _ in range(len(a))] for _ in range(2)]

    for i in range(len(a)):
        if left > a[i]:
            left = a[i]
        maps[0][i] = left
    
    for i in range(len(a)-1, -1, -1):
        if right > a[i]:
            right = a[i]
        maps[1][i]=right
    print(maps)    
    for i in range(len(a)):
        if a[i] <= maps[0][i] or a[i]<= maps[1][i]:
            answer+=1
    

    
    

    
    return answer


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))