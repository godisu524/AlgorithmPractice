def solution(n):
    answer = 0
    while len(list(str(n)))!=1:
        print(n)
        nums = list(str(n))
        mid = len(list(str(n)))//2


        left_num = nums[:mid]
        right_num = nums[mid:]

        while(right_num[0]=="0"):
            left_num.append(right_num.pop(0))




        n = eval("".join(left_num)+"+"+"".join(right_num))
        answer +=1
    return [answer,n]
    #if right_num = 

    
    return answer



print(solution(9))