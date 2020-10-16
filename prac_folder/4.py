def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse= True)
    for _ in range(len(A)):
        answer+=A[_]*B[_]
    return answer

print(solution([1, 4, 2],	[5, 4, 4]))