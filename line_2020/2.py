import heapq
import random

def solution(ball, order):
    answer = []
    max_value = 1
    q=[]
    ball_length = len(ball)


    def ball_check(array,b):
        
        if array[-1] == b :
            answer.append(array.pop())
            return True
        elif array[0] == b :
            answer.append(array.pop(0))
            return True
        return False

    pre_ball = ball.copy()
    for o in order:
        #보류중인 것들 먼저확인
        #print(ball,q,answer)
        tempq = []
        
        if ball != pre_ball:
            while(ball != pre_ball):
                pre_ball = ball.copy()
                for i in range(len(q)):
                    temp =heapq.heappop(q)
                    if ball_check(ball,temp[1]):
                        continue
                    else:
                        heapq.heappush(tempq,temp)
                q = tempq.copy()
        #오더 확인.
        if ball_check(ball,o):
            continue
        else:
            heapq.heappush(q,(max_value,o))
            max_value+=1
    
            

    return answer


ball = [i for i in range(1,100)]
order = ball.copy()
random.shuffle(order)

print(ball)
print(order)
print(solution(ball	,order))