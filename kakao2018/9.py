import copy

#매트릭스를 90% 회전시켜주는 코드
def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0]* n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i -1] = a[i][j]
    return result

def check(m, n, board):
    temp = board[m][n]
    if board[m][n+1] == temp:
        if board[m+1][n+1]==temp:
            if board[m+1][n]==temp:
                return True
def update_board(m,n,board):
    while True:
        temp=copy.deepcopy(board)
        #print(temp,1)
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]!= 0:
                    
                    if board[i+1][j]==0:
                        board[i+1][j]=board[i][j]
                        board[i][j]=0
        #print(board,2)
        #print(temp,3)
        if board == temp:
            return copy.deepcopy(board)
        

def solution(m, n, board):
    board = rotate_a_matrix_by_90_degree(board)

    answer = 0
    delete=set()
    while True: 
        
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0:
                    if check(i,j,board):
                        delete.add((i,j))
                        delete.add((i+1,j))
                        delete.add((i,j+1))
                        delete.add((i+1,j+1))
        if len(delete) == 0:
            break
        for d in delete:
            board[d[0]][d[1]] = 0
        

        delete.clear()
        #print(board)
        board=update_board(m,n,board)
        #print(board)

  

        
     
        #break


    for i in range(m):
        for j in range(n):
            if board[i][j]==0:
                answer+=1  

    
    
    return answer



print(solution(6,6, ["AABBEE","AAAEEE","VAAEEV","AABBEE","AACCEE","VVCCEE"]))