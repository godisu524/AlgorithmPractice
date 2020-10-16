for tc in range(int(input())):
    n, m = map(int,input().split())
    array = list(map(int,input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    
    for j in range(1,m):
        for i in range(n):
            if i ==0:
                left_up =0
            else:
                left_up = dp[i-1][j-1]
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
        
            left = dp[i][j-1]
            dp[i][j]= dp[i][j]+max(left_down,left_up,left)
    result = 0
    #result 가 결국 더적은게 나올수도있으니까 다비교하면서 리절트값으로해야함. 4번움직여야하니까 무조건 마지막값만 보면됨.
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)
                
        