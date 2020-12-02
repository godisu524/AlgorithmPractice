from itertools import combinations
from collections import Counter

def solution(s, n):
    answer=[]
    done = []
    ss = set(s)
    counts= {}
    for alp in ss:
        counts[alp]=s.count(alp)
    for alp in counts:
        counts[alp] -= n
    print(counts)
        
    
    



print(solution("aaaaaaaabbbbbcccccccdddddddddddddd",5))