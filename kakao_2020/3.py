import heapq
from bisect import bisect_left, bisect_right
from collections import OrderedDict
def count_range(array,x,y):
    right = bisect_right(array,y)
    left = bisect_left(array,x)
    return right - left





def solution(info, query):
    people=[]
    answer = [0 for _ in range(len(query))]
    for text in info:
        language, position, freshness, soulfood, grade = text.split()
        #people[int(text.split()[-1])]=(text.split()[1:-1])
        
        heapq.heappush(people,(int(grade),language, position, freshness, soulfood))
        
    
    grades=[]
    #print(people)
    for a in people:
        grades.append(a[-1])
    
    
    
    

    #print(people)
    
    for n,q in enumerate(query):
        #print(n)
        q= q.split()
        soulfood = q[6]
        language = q[0]
        position= q[2]
        freshness = q[4]
        grade = int(q[-1])
        
        index = bisect_left(grades,grade)
        for i in range(index,len(people)):
            if soulfood != "-":
                if soulfood != people[i][3]:
                    continue
            if language != "-":
                if language != people[i][0]:
                    continue
            if position != "-":
                if position != people[i][1]:
                    continue
            if freshness != "-":
                if freshness != people[i][2]:
                    continue
            if int(grade) <= int(people[i][-1]):
                #print(grade,person[-1])
                answer[n]+=1
                #print("yes")

        

        
        #print(language, position, freshness, soulfood, grade)
        
        
    









    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))