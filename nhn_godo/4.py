def solution(cardNumber):
    cardNumber= list(map(int,cardNumber))
    if len(cardNumber)%2 ==1:
        for i in range(len(cardNumber)):
            if i %2 ==1:
                cardNumber[i] *=2
    else:
        for i in range(len(cardNumber)):
            if i %2 ==0:
                cardNumber[i] *=2
    total_ans = []

    for num in cardNumber:
        for n in list(str(num)):
            total_ans.append(int(n))
    
    if sum(total_ans) %10 ==0:
        return "VALID"
    else:
        return "INVALID"


print(solution("26227174957722514961366"))