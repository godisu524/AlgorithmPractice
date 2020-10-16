
def solution(land):
    answer = 0
    
    dp = [[0 for i in range(len(land[0]))] for _ in range(len(land))]
    dp[0]=land[0]
    for i in range(1,len(dp)):
        for j in range(len(dp[0])):
            temp=[]
            for m in range(len(dp[0])):
                if m  != j:
                    temp.append(dp[i-1][m])
            dp[i][j]=max(temp)+land[i][j]

    #print(dp)
    

    return max(dp[-1])


print(solution([[1,2,3,5],
[5,6,7,100],
[4,3,2,1]]))

