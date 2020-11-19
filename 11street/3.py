import decimal
def solution(X, Y):
    counts={}

    
    for i in range(len(X)):
        try:
            counts[round(X[i]/Y[i],10)]+=1
        except:
            counts[round(X[i]/Y[i],10)]=1
    max_count=0
    for count in counts:
        max_count = max(counts[count],max_count)

    print(counts)
    return max_count


        
print(solution([1, 2, 3, 4, 0 , 12], [2, 3, 6, 8, 4 , 18]))