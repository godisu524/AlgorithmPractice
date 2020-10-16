# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque
def solution(A, K):
    # write your code in Python 3.6
    A= deque(A)
    A.rotate(K)
    
    
    return list(A)


print(solution([3,4,5,6,7,8],3))