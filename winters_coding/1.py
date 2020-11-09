def solution(n, delivery):
    
    answer=["?" for i in range(n+1)]
    for d in delivery:
        if d[2] == 1:
            answer[d[0]] = "O"
            answer[d[1]] = "O"
    
    for d in delivery:
        if d[2]==0:
            if answer[d[0]] =="O":
                answer[d[1]] = "X"
            elif answer[d[1]] == "O":
                answer[d[0]] = "X"
    return "".join(answer[1:])
   

            



print(solution(6,	[[1,3,1],[3,5,0],[5,4,0],[2,5,0]]))