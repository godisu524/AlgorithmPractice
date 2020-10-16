def solution(n, s):
    answer = []
    if n>s :
        return [-1]
    index = s//n
    temp = s%n

    
    for _ in range(n):
        answer.append(index)
    length = n-1
    for _ in range(temp):
        answer[length]+=1
        length-=1
    


    
    

    return sorted(answer)

print(solution(3,11))