#재귀함수 이용
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def solution(N):
    answer=[0,0]
    for i in range(2,10):
        sol=1
        temp_num=convert(N,i)
        for num in list(str(temp_num)):
            if num != "0":
                sol*=int(num)
        if sol >= answer[1]:
            answer = [i,sol]
    return answer


print(solution(1400000000))