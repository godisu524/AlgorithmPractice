from itertools import product
n,m = map(int,input().split())

coins = list(map(int,input().split()))
count=0
for a in list(product(coins,repeat= 2)):
    if a[0]!=a[1]:
        count+=1


print(count//2)