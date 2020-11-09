n =  int(input())


box=0

while True:
    if n %5 == 0:
        box = box + (n//5)
        print(box)
        break

    n -= 3
    box+=1
    if n<0:
        print(-1)
        break