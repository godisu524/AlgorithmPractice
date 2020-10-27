def solution(triangle):
    answer = 0

    dp = [[0 for _ in range(len(triangle[-1]))]for i in range(len(triangle))]
    #print(dp)
    dp[0][0] = triangle[0][0]
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j==0:
                up_left=0
            else:
                up_left=dp[i-1][j-1]
            
            if j == len(triangle[i]):
                up_right = 0
            else:
                up_right = dp[i-1][j]

            dp[i][j]= max(up_left,up_right)+triangle[i][j]


    #for d in dp:
    #    print(d)
    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	))