import datetime
def change_time(customer):
    customer = "".join(customer)
    #print(customer.split()[0].split("/")[0])
    myDatetime = datetime.datetime.strptime('2021-'+customer.split()[0].split("/")[0]+'-'+customer.split()[0].split("/")[1]+' '+customer.split()[1], '%Y-%m-%d %H:%M:%S')
    return myDatetime
    #datetime(2020,int(customer.split()[0].split("/")[0]),int(customer.split()[0].split("/")[1]),int(customer.split()[1].split(":")[0]),int(customer.split()[1].split(":")[1]),int(customer.split()[1].split(":")[2]))



    
    

print(datetime.datetime(2016,5,24).weekday())

def solution(n, customers):
    answer= 0
    
    kiosk = [[]for _ in range(n)]
    able_time =[[]for _ in range(n)]
    
    score_time = [0 for _ in range(n)]
    
    
    #초기화끝
    for i in range(n):
        try:
            kiosk[i].append(customers.pop(0))
            score_time[i]+=1
        except:
            break
    
    for i in range(n):
        able_time[i] = change_time(kiosk[i]) +datetime.timedelta(minutes=int(kiosk[i][0].split()[2]))

    
    
    for customer in customers:
        
        temp=[]
        customer_temp_time= change_time(customer)
        #update
        for i in range(n): 
            if able_time[i] < customer_temp_time:
                kiosk[i].clear()
        for i in range(n):
            if len(kiosk[i]) == 0:
                temp.append(i)
        if len(temp)==1:
            kiosk[temp[0]].append(customer)
            able_time[temp[0]] = change_time(kiosk[temp[0]]) +datetime.timedelta(minutes=int(kiosk[temp[0]][0].split()[2]))
            score_time[temp[0]]+=1
            
        elif len(temp)>1:
            maximum = able_time[temp[0]]
            index=0
            for t in temp[1:]:
                if able_time[t] < maximum:
                    maximum = able_time[t]
                    index = t
            
            kiosk[index].append(customer)
            
            able_time[index] = change_time(kiosk[index]) +datetime.timedelta(minutes=int(kiosk[index][0].split()[2]))
            score_time[index]+=1
            
        else:
            t = able_time.index(min(able_time))
            kiosk[t].append(customer)
            able_time[t] = able_time[t] +datetime.timedelta(minutes=int(kiosk[t][-1].split()[2]))
            score_time[t]+=1


    
    return max(score_time)


print(solution(3,["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]	))