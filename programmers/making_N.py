def solution(N, number):

    if N == number:
        return 1
    dp = [set() for x in range(8)]

    for i,x in enumerate(dp,start=1):
        x.add(int(str(N)*i))

    for i in range(1,8):
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i-j-1]:
                    dp[i].add(op1+op2)
                    dp[i].add(op1-op2)
                    dp[i].add(op1*op2)

                    if op2 != 0:
                        dp[i].add(op1//op2)
        if number in dp[i]:
            answer = i +1
            break
        else:
            answer=-1


    return answer



print(solution(5,12))
    
    
