def is2x2(m, n, board):
    answer = [] 
    for i in range(m-1): 
        for j in range(n-1): 
            temp = board[i][j] 
            if temp == 0: 
                continue 
            if temp == board[i+1][j] and temp == board[i][j+1] and temp == board[i+1][j+1]: 
                answer += [[i, j], [i+1, j], [i, j+1], [i+1, j+1]] 
    return list(set(map(tuple, answer))) 
                #중복된 원소를 삭제하기 위해 set으로 바꿨다 리스트로 다시 변환 
def removeBlock(m, board, l): 
    for i in l: 
        board[i[0]].pop(i[1]) 
    for j in range(m): 
        if len(board[j]) < m: 
            board[j] += [0] * (m - len(board[j])) 
    return board 

def solution(m, n, board): 
    board = list(map(list, zip(*board[::-1])))
    #보드를 시계방향으로 90도 회전 
    m, n = n, m 
    
    answer = 0 
    
    while(True): 
        temp = is2x2(m, n, board) 
        if temp == []: 
            break 
        answer += len(temp) 
        board = removeBlock(m, board, sorted(temp, reverse = True)) #---(*) 
    
    return answer


print(solution(6,6, ["AABBEE","AAAEEE","VAAEEV","AABBEE","AACCEE","VVCCEE"]))
