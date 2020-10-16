import heapq
def change_time_to_sec(time):
    times = list(map(int,time.split(":")))
    time = times[0]* 3600 +times[1] * 60 + times[2]
    return time

def change_sec_to_time(time):
    hours=str(time//3600)
    time = time%3600
    mins=str(time//60)
    secs=str(time%60)

    if len(hours) ==1:
        hours ="0"+ str(hours)
    if len(mins) ==1:
        mins = "0" + str(mins)
    if len(secs) == 1:
        secs = "0" + str(secs)
    return str(hours)+":"+str(mins)+":"+str(secs)


def solution(play_time, adv_time, logs):


    answer = ''
    play_time=change_time_to_sec(play_time)
    
    adv_time=change_time_to_sec(adv_time)

    if play_time == adv_time:
        return "00:00:00"

    people= []
    starts=[]
    #logs.sort()
    #print(logs)
    for a in logs:
        heapq.heappush(people,(change_time_to_sec(a.split("-")[0]),change_time_to_sec(a.split("-")[1])))
        heapq.heappush(starts,change_time_to_sec(a.split("-")[0]))
    #print(people)
    max_count=0
    max_time=0
    
    iteration=len(starts)
    for aaa in range(len(starts)):
        
        i = heapq.heappop(starts)
        people_copy = people.copy()
        count=0
        temp=set(range(i,i+adv_time))
        for _ in range(len(people_copy)):
            person = heapq.heappop(people_copy)
            count += len(temp.intersection(range(person[0],person[1])))
        if count > max_count:
            max_count=count
            max_time = i
    

        
            
    #print(max_time,max_count)
    #print(change_sec_to_time(max_time),change_sec_to_time(max_count))
    #print(change_sec_to_time(max_time))
    return change_sec_to_time(max_time)
            


    


    


print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))