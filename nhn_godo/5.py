def solution(votes):
    count=0
    while True:
        print(votes)
        if votes[0] == max(votes) :
            if votes.count(votes[0]) ==1:
                return count
            else:
                return count + 1
        
        else:
            votes[votes.index(max(votes))] -=1
            votes[0]+=1
            
            count+=1


print(solution([100]))