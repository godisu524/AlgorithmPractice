def solution(a, b):
    answer = 0
    
    if a == b:
        return a
    
    if a > b:
        a,b=b,a
    answer =(b*(b+1))//2 - (a-1)*(a)//2
    return answer


print(solution(3,5))