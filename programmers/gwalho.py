def checkBracket(text): #균형잡혔을 때, 올바른지 체크,
    openBracket = 0
    closeBracket = 0
    for bracket in text:
        if bracket == '(':
            openBracket += 1
        else:
            closeBracket += 1
        if openBracket < closeBracket:
            return False
    
    return True

def divideBracket(p):
    if p == '':
        return '' 
    openBracket = 0
    closeBracket = 0
    lastBracket = ''

    for index in range(len(p)):
        if p[index] == '(':
            openBracket += 1
        else:
            closeBracket += 1
        lastBracket = p[index]
        if openBracket == closeBracket:
            if lastBracket == ')': # 수가 같은데 닫혔으면 올바르다.
                # u가 올바르면 # 뒤에도 똑같이 진행하면 된다. 그 값을 더해서 반환
                return p[:index+1] + divideBracket(p[index+1 :])
            else: # 안 올바르다 균형은 잡혔다.
                # 앞에꺼 올바르게 고치기 -> 뒤에꺼 나누기
                return reverse(p[:index+1], divideBracket(p[index+1 :]))

def reverse(u, v) : # 앞 뒤 뒤집어서 v 붙여서 더함. v도 다 마친 상태.
    empty = '('
    empty += v + ')'
    for i in range(1, len(u)-1):
        if u[i] == '(':
            empty += ')'
        else:
            empty += '('
    return empty

def solution(p):
    if checkBracket(p):
        return p
    
    return divideBracket(p)
print(solution(")("))