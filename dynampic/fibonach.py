def solution(n):
    d=[0]*(n+1)
    d[1]=1
    d[0]=0
    d[2]=2
    if n ==1 or n ==2:
        return n
    else:
        #print(1)
        for i in range(3,n+1):
            d[i]=d[i-1]+d[i-2]
    return int(d[n]%1000000007)


print(solution(6))
