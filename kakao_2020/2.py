from itertools import combinations
def solution(orders, course):
    answer = []
    for n,order in enumerate(orders):
        orders[n] = "".join(sorted(list(order)))
        
    #orders.sort()
    
    total_combination=[[] for _ in range(len(orders))] 
    for n,i in enumerate(course):
        for order in orders:
            for index in list(combinations(order,i)):
                total_combination[n].append(index)
    #print(total_combination)
    for total in total_combination:
        max_count =2
        max_values=[]
        for a in total:
            print(a)
            if total.count(a) >= max_count :
                max_count = total.count(a)
                if a not in max_values:
                    max_values.append(a)
        for values in max_values:
            if total.count(values) == max_count:
                answer.append(values)
    answer.sort()
    #print(answer)
    real_answer=[]
    for a in answer:
        real_answer.append("".join(a))    

    
    return real_answer



print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))