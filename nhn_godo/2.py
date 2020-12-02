def solution(page, broken):
    ans=[""]
    answers=[]
    start = 100
    if page == start:
        return 0
    max_value = abs(page - start)
    answers.append(max_value)
    if len(broken) == 10:
        return max_value

    pages = list(map(int,str(page)))
    for p in pages:
        if p not in broken:
            for i in range(len(ans)):
                ans[i]+=str((p))
        else:
            index=1
            finish=False
            while True:
                if finish:
                    break
                if p-index >=0 and (p - index) not in broken:
                    for i in range(len(ans)):
                        ans[i]+=str(p-index)
                    finish = True
                if p+index <=9 and (p + index) not in broken:
                    for i in range(len(ans)):
                        ans[i]+=str(p+index)
                    finish = True
                index+=1
    
    for a in range(len(ans)):
        if len(ans[a]) != 1:
            ans.append(ans[a][:-1])
        ans.append(ans[a]+ans[a][-1])
    
    
    print(ans)
    for a in ans:
        answers.append(abs(page-int(a)) + len(a))

    print(answers)
    


    
    return min(answers)
    
        
    
    
    #return len(ans)+page-int("".join(ans))
    
                    

                
    





print(solution(151241,[0,1,2,3,4,7,8,9]))