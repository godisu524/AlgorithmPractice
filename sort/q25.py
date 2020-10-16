n= int(input())
stages = list(map(int,input().split()))
array =[]
for i in range(1,n+1):
    cnt=0
    for stage in stages:
        if stage >=i:
            cnt+=1
    array.append([i,stages.count(i)/cnt])

array.sort(key = lambda x: x[1], reverse = True)

for a in array:
    print(a[0])

