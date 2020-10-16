n = list(map(int,input()))
num=0
for i in n:
    if i == 0:
        continue
    else:
        if num == 0:
            num+= i
        else:
            num*=i

print(num)