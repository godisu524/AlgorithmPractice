#진법수로 바꾸기
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]



def solution(n, t, m, p):
    answer = ''
    i=0
    t2=0
    finish_flag=False
    turn=1
    while True:
        if finish_flag:
            break
        num=convert(i,n)
        num=list(str(num))
        while num:
            
            if finish_flag:
                break
            temp=num.pop(0)
            if turn ==p:
                answer+=temp
                t2+=1
                if t2==t:
                    finish_flag=True
                    break
            turn +=1
            if turn == m+1:
                turn =1
        i+=1

    
    return answer


print(solution(16,	16,	2,	2))