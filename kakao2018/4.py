def solution(files):
    answer = []
    temp=files.copy()
    
    for file in files:
        answer.append(file.lower())
    files=[]
    for i,file in enumerate(answer):
        now=0
        files.append([[],[],[]])

        for s in file:
            if s.isdigit() and now==0:
                now+=1
            if not s.isdigit() and now==1:
                now+=1
            files[i][now].append(s)
        files[i].append(i)
    for n,file in enumerate(files):
        for m,f in enumerate(file[:-1]):
            files[n][m] = "".join(f)
    
    #files.sort(key = lambda x: x[2])
    files.sort(key = lambda x: int(x[1]))
    files.sort(key = lambda x: x[0])


    answer.clear()
    for file in files:
        answer.append(temp[file[-1]])


    #answer.sort(key = lambda x:x.split(".")[0])
    #print(answer)

    
    return answer


print(solution( ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

