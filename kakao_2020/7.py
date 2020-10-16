from collections import deque
def solution(sales, links):
    answer = 0
    n= len(sales)

    visited=[]
    q = deque()
    array = [[0] for _ in range(n+1)] 
    for link in links:
        a,b = link[0],link[1]
        array[a].append(b)
    dist = 1
    teams=[[] for _ in range(n+1)]
    #print(teams)
    visited.append(1)
    for i in array[1][1:]:
        q.append(i)
        teams[1].append(i)
        visited.append(i)
    #print(array)
    #print(q)
    leaders=[]
    while q:
        #print(q)
        length = len(q)
        for i in range(length):
            a = q.popleft()
            visited.append(a)
            if len(array[a]) ==1:
                continue
            leaders.append(a)
            visited.append(a)
            for index in array[a][1:]:
                if index not in visited:
                    q.append(index)
                    teams[a].append(index)
    #print(teams)
    def check_min(leader):
        person=[]
        min_person= sales[leader-1]
        
        for a in teams[leader]:
            #print(a)
            min_person = min(min_person,sales[a-1])
            person.append(a)
        return person, min_person


    while leaders:
        #print(leaders)
        leader = leaders.pop(0)
        person,min_person = check_min(leader)
        if person in leaders:
            person2,min_person2 = check_min(person)
            if person != person2:
                answer += min_person
            else:
                answer += min_person
                leaders.remove(person)
            
        else:
            answer += min_person
    
        

        

        
        

    
    







    return answer

print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))
