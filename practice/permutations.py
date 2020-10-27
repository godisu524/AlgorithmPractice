#[Programmers] 프로그래머스 파이썬 > 줄 서는 방법
# permutations를 활용한 풀이 - 실패
'''
from itertools import permutations
def solution(n, k):
    nl = [i for i in range(1,n+1)]
    return list(permutations(nl,n))[k-1]
'''

# 예시 : factorial 활용
from math import factorial
def solution(n, k):
    answer = []
    nl = list(range(1,n+1))
    while n!=0 :
        fact = factorial(n-1)
        answer.append(nl.pop((k-1)//fact))
        n -= 1
        k %= fact
    return answer