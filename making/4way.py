n = int(input())
waylist= list(input().split())

#my_map = [[0]*n for m in range(n)]
startx, starty = 1,1
for way in waylist:
    if way == "L":
        if startx -1 != 0:
            startx -=1 
    elif way == "R":
        if startx +1 != 6:
            startx +=1 
    elif way == "U":
        if starty -1 != 0:
            starty -=1 
    else :
        if starty +1 != 0:
            starty +=1 

print(starty,startx)






