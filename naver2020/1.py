def solution(blocks):
    answer=[]
    #print(len(blocks))
    answer=[-101 for i in range((len(blocks)*(len(blocks)+1))//2+1)]
    
    step = 1
    count=1
    for block in blocks:
        answer[step + block[0]] = block[1]
        step+=count
        count+=1
    
    while True:
        #print(123)
        step = 2
        temp_count = 0
        total_range=[2,4]
        if answer.count(-101) ==1:
            break
        for n in range(2,len(answer)) :
            temp_count+=1
            #print(step,n,total_range)
            if answer[n] != -101:
                if answer[n-1] ==-101 and n-1 in range(total_range[0],total_range[1]):
                    answer[n-1]= answer[n-step]-answer[n]
                    break
                elif n+1 in range(total_range[0],total_range[1]):
                    if answer[n+1] ==-101 :
                        answer[n+1]= answer[n+1-step]-answer[n]
                        break
            
            if temp_count == step:
                step+=1
                temp_count = 0
                total_range[0]=total_range[1]
                total_range[1]+=step
        #print(answer)
        
        
        
           

    



    
    
    
    
    
    
    return answer[1:]

print(solution([[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]))
