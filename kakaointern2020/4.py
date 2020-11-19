from itertools import combinations

att = int(input())
t = float(input())
n = int(input())

attributes=[]


mdic={}
for i in range(n):
    attributes.append(input().split(","))
for a in attributes:
    for comb in combinations(a,att):
        comb=list(comb)
        comb.sort()
        comb=tuple(comb)
        try:
            mdic[comb] +=1
        except:
            mdic[comb] = 1
ans=[]
for m in mdic:
    if mdic[m]/n >= t:
        print(",".join(m))
    



