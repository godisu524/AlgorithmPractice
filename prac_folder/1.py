def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(i,j)
            if  i != j:
                temp =numbers[i] + numbers[j]
                if temp not in answer:
                    answer.append(temp)
    answer.sort()
    return answer

print(solution([2, 1, 3, 4, 1]))