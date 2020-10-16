def solution(s):
    answer = ''
    m_f= False
    s_f = False
    numbers=[]
    num=""
    for a in s:
        if a==" ":
            if m_f:
                numbers.append(-int(num))
                m_f=False
                num=""
            else:
                numbers.append(int(num))
                num=""
        elif a=="-":
            m_f = True
        else:
            num+=a
    if m_f:
        numbers.append(-int(num))
        m_f=False
        num=""
    else:
        numbers.append(int(num))
        num=""
            
    answer+=str(min(numbers))+" "
    answer+=str(max(numbers))

    return answer



print(solution("-1 -2 -3 -4"))