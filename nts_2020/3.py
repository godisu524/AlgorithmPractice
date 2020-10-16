def solution(histogram):
    answer = 0
    for i in range(len(histogram)):
        for j in range(i+1,len(histogram)):
            if histogram[i] > histogram[j]:
                print(i,j)
                answer = max(answer,((j-i)-1)*histogram[j])
    if answer == 0:
        return sex

    return answer


()


print(solution([2,2,2,4]))