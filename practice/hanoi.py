

def solution(n):
    answer=[]
    answer =hanoi(n, 1, 2, 3,answer)

    return answer


def hanoi(n, a, b, c,answer):
    if n == 1:
        answer.append([a,c])
        return answer
    else:
        hanoi(n - 1, a, c, b,answer)
        answer.append([a,c])
        hanoi(n - 1, b, a, c,answer)
        
    return answer



print(solution(2))