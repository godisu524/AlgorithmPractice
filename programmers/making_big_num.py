from itertools import permutations



def solution(number, k):
    collected =[]
    for i,num in enumerate(number):
        print(collected)
        while len(collected)>0 and collected[-1] < num and k>0:
            print(collected)
            collected.pop()
            k-=1
        if k==0:
            collected+= list(number[i:])
            break
        collected.append(num)
    print(collected)
    #collected = collected[:-k] if k>0 else collected

    answer = ''.join(collected)
    return answer
        
print(solution("4177252841",4))