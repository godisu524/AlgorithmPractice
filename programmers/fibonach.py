def solution(n):
    d=[0]*(n+1)
    if n ==1 or n ==2:
        return n
    else:
        if d[n] != 0:
            return d[n]
        else:
            d[n] = solution(n-1)+solution(n-2)
            return int(d[n]%1000000007)

    
    


print(solution(6000))

