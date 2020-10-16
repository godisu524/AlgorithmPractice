n,m = map(int,input().split())

A=list(map(int,input().split()))
B= list(map(int,input().split()))

A.sort()
B.sort(reverse = True)

for i in range(n):
    if m ==0:
        break
    if A[i] < B[i]:
        A[i],B[i] = B[i],A[i]
        m-=1
print(sum(A))