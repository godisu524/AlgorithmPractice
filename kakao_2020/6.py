def solution(board, r, c):
    answer = 0
    temp = 0

    

    def move_left(r,c):
        if c-1 >=0:
            return r, c-1
    def move_right(r,c):
        if c+1 <=3:
            return r, c+1
    def move_up(r,c):
        if r-1 >=0:
            return r-1,c
    def move_down(r,c):
        if r+1 <=3:
            return r+1,c

    def find_pos[]
    
        
        


    if board[r][c] != 0:
        temp = board[r][c]

        
    





    return answer



print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0))