def solution(goods):
    temp=[]
    total=0
    for good in goods:
        if good <50:
            temp.append(good)
            if sum(temp) >=50:
                total+=sum(temp)-10
                temp.clear()
        else:
            total+=good-10
    total+=sum(temp)
    
    return total


print(solution([46,62,9]))