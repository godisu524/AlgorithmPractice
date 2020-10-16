def solution(N):
    answer=[]
    for a in range(1,N//2+1):
        answer.append(a)
        answer.append(-a)
    if N %2 ==1:
        answer.append(0)
        return answer
    else:
        return answer


print(solution(1))
