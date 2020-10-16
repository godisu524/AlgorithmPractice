from bisect import bisect_left,bisect_right


def count_range(array,x,y):
    right = bisect_right(array,y)
    left = bisect_left(array,x)
    return right - left


array = [[] for _ in range(10001)]
reversed_array=[[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word).append(word)]
        reversed_array[len(word)].append(word[::-1])
    
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0] !='?':
            res = count_range(array[len(q)],q.replace('?','a'),q.replace('?','z'))
        else:
            res = count_range(reversed_array[len(q)],q.replace('?','a'),q[::-1].replace('?','z'))
        answer.append(res)
    return answer