for i in range(1,91):
    n = i

    dp = [0 for i in range(n+5)]

    dp[0]= 0
    dp[1]=1
    dp[2]=1


    if n <3 :
        print(dp[n])

    else:
        for i in range(3,n+1):
            dp[i] = dp[i-2]+dp[i-1]

        print(dp[n])
