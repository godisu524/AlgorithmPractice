def solution(flowers):
    answer = 0
    opened=set()
    for flower in flowers:
        for a in range(flower[0],flower[1]):
            opened.add(a)
    
    return len(opened)

print(solution([[2, 5], [3, 7], [10, 11]]))